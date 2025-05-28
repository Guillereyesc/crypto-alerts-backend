import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_analisis(signals):
    prompt = f"""
Actúa como un analista técnico experto. Recibiste estas señales:
- {chr(10).join(signals)}

Entrega:
1. Tipo de operación sugerida (compra/venta)
2. Explicación de la oportunidad
3. Nivel ideal de entrada, stop loss y take profit (en base genérica)
4. Confianza en la señal (alta si ≥ 3 señales fuertes)
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response["choices"][0]["message"]["content"]
