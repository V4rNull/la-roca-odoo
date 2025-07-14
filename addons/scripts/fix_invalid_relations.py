def run(env):
    models_to_clean = [
        ('la_roca.bitacora', 'persona_id'),
        ('la_roca.bitacora', 'responsable_id'),
        ('la_roca.historial', 'persona_id'),
        ('la_roca.historial', 'responsable_id'),
        ('la_roca.confrontacion', 'persona_id'),
        ('la_roca.confrontacion', 'responsable_id'),
    ]

    for model_name, field_name in models_to_clean:
        try:
            Model = env[model_name]
            broken = Model.search([('%s' % field_name, '!=', False)])
            deleted_count = 0
            for rec in broken:
                try:
                    getattr(rec, field_name).id
                except Exception:
                    rec.unlink()
                    deleted_count += 1
            print(f"[✓] Limpiados {deleted_count} registros con {field_name} roto en {model_name}")
        except Exception as e:
            print(f"[✗] Error en {model_name}.{field_name}: {e}")
