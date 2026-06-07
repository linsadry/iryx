import json

def load(p):
    try:
        d = json.load(open(p))
        return d if isinstance(d, list) else []
    except Exception as e:
        print(f"Aviso: {p}: {e}")
        return []

date = open('/tmp/backup_date.txt').read().strip()

backup = {
    'version': '2.1',
    'exported_at': date,
    'tables': {
        'iryx_transactions': load('/tmp/tx.json'),
        'iryx_goals':        load('/tmp/goals.json'),
        'iryx_budgets':      load('/tmp/budgets.json'),
        'iryx_clinicas':     load('/tmp/clinicas.json'),
        'iryx_turnos':       load('/tmp/turnos.json'),
    }
}

out = f'backups/{date}.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(backup, f, ensure_ascii=False, indent=2)

print(f"Backup: {out}")
for k, v in backup['tables'].items():
    print(f"  {k}: {len(v)} registros")
