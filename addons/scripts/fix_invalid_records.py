def run(env):
    models = [
        'la_roca.confrontacion',
        'la_roca.historial',
        'la_roca.bitacora',
    ]
    for model in models:
        records = env[model].search([])
        count = 0
        for rec in records:
            if hasattr(rec, 'persona_id') and not rec.persona_id:
                rec.unlink()
                count += 1
                continue
            if hasattr(rec, 'responsable_id') and not rec.responsable_id:
                rec.unlink()
                count += 1
        print(f"[✓] Limpiados {count} registros rotos de {model}")
