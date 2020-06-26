#! python3
# pw.py - Niebezpieczny program menedżera haseł.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Użycie: py pw.py [konto] — skopiowanie hasła wskazanego konta')
    sys.exit()

account = sys.argv[1] # Pierwszym argumentem wiersza poleceń jest nazwa konta.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło do konta ' + account + ' zostało skopiowane do schowka.')
else:
    print('Nie istnieje konto o nazwie ' + account + '.')
