#! python3
# Sprawdza polecenia otrzymywane przez e-mail i wykonuje je.
# Ten program przeprowadza sprawdzenie pod kątem łączy BitTorrent "magnet",
# oraz uruchamia program qBittorrent w celu użycia tych łączy.

import smtplib, imapclient, pyzmail, logging, traceback, time, subprocess
logging.basicConfig(filename='torrentStarterLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Konfiguracja programy przez zdefiniowanie pewnych zmiennych.
MY_EMAIL = 'mój_adres_email@gmail.com' # Bot powinien reagować tylko na mnie.
BOT_EMAIL = 'imaptest@coffeeghost.net'
BOT_EMAIL_PASSWORD = '7|)6S1JS6>euu8p/nTlf'
IMAP_SERVER = 'mail.coffeeghost.net'
SMTP_SERVER = 'mail.coffeeghost.net'
SMTP_PORT = 465
TORRENT_PROGRAM = 'C:\\Program Files (x86)\\qBittorrent\\qbittorrent.exe'

assert BOT_EMAIL != MY_EMAIL, "Przydziel botowi jego własny adres e-mail."


def getInstructionEmails():
    # Logowanie do poczty elektronicznej.
    logging.debug('Nawiązanie połączenia z serwerem IMAP %s...' % (IMAP_SERVER))
    imapCli = imapclient.IMAPClient(IMAP_SERVER, ssl=True)
    imapCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    imapCli.select_folder('INBOX')
    logging.debug('Nawiązano połączenie.')

    # Pobranie wszystkich wiadomości e-mail z poleceniami.
    instructions = []
    UIDs = imapCli.search(['FROM ' + MY_EMAIL])
    rawMessages = imapCli.fetch(UIDs, ['BODY[]'])
    for UID in rawMessages.keys():
        # Przetworzenie wiadomości e-mail.
        message = pyzmail.PyzMessage.factory(rawMessages[UID]['BODY[]'])
        if message.html_part != None:
            body = message.html_part.get_payload().decode(message.html_part.charset)
        if message.text_part != None:
            # Jeżeli wiadomość zawiera zarówno część html, jak i tekstową, należy użyć części tekstowej.
            body = message.text_part.get_payload().decode(message.text_part.charset)

        # Wyodrębnienie poleceń z treści wiadomości.
        instructions.append(body)

    # Usunięcie wiadomości z poleceniami, o ile takie istnieją.
    if len(UIDs) > 0:
        imapCli.delete_messages(UIDs)
        imapCli.expunge()

    imapCli.logout()

    return instructions


def parseInstructionEmail(instruction):
    # Wysłanie wiadomości e-mail z informacjami o zadaniu.
    responseBody = 'Subject: Polecenie zostało wykonane.\nPolecenie zostało otrzymane i wykonane.\nOdpowiedź:\n'

    # Przetworzenie treści wiadomości e-mail w celu odczytu poleceń.
    lines = instruction.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            subprocess.Popen(TORRENT_PROGRAM + ' ' + line) # Uruchomienie programu klienta bittorrent.
            responseBody += 'Pobieranie łącza magnet.\n'

    # Wysłanie wiadomości e-mail z potwierdzeniem, że bot wykonał polecenie.
    logging.debug('Nawiązanie połączenia z serwerem SMTP %s i wysłanie potwierdzenia...' % (SMTP_SERVER))
    #smtpCli = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)     # Usuń znak komentarza z odpowiedniego wiersza (ten lub poniższy).
    smtpCli = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # Usuń znak komentarza z odpowiedniego wiersza (ten lub powyższy).
    smtpCli.ehlo()
    #smtpCli.starttls() # Usuń znak komentarza na początku wiersza, jeśli używasz SMTP_SSL.
    smtpCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    logging.debug('Nawiązano połączenie.')
    smtpCli.sendmail(BOT_EMAIL, MY_EMAIL, responseBody)
    logging.debug('Wysłano wiadomość e-mail z potwierdzeniem.')
    smtpCli.quit()


# Rozpoczęcie działającej w nieskończoność pętli, która sprawdza wiadomości e-mail i wykonuje zawarte w nich polecenia.
print('Bot pocztowy rozpoczął pracę. Naciśnij Ctrl-C, aby zakończyć jego działanie.')
logging.debug('Bot pocztowy rozpoczął pracę.')
while True:
    try:
        logging.debug('Pobieranie poleceń z wiadomości e-mail...')
        instructions = getInstructionEmails()
        for instruction in instructions:
            logging.debug('Wykonywanie poleceń: ' + instruction)
            parseInstructionEmail(instruction)
    except Exception as err:
        logging.error(traceback.format_exc())

    # Sprawdzenie odbywa się co 15 minut.
    logging.debug('Zakończono przetwarzanie poleceń. Teraz trwa 15-minutowa przerwa.')
    time.sleep(60 * 15)
