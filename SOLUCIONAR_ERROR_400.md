# 🔴 ERROR 400: redirect_uri_mismatch - SOLUCIÓN

## ❌ ¿Por qué no es válido?

El error **"Error 400: redirect_uri_mismatch"** significa que la URI que Django está enviando a Google **NO está configurada** en tu proyecto de Google Cloud Console.

Google rechaza la solicitud porque la URI de retorno no coincide con las URIs autorizadas.

---

## ✅ SOLUCIÓN: Agregar las URIs en Google Cloud Console

### 📋 PASO A PASO:

#### 1. Ve a Google Cloud Console
**URL:** https://console.cloud.google.com/apis/credentials

#### 2. Busca tu OAuth 2.0 Client ID
Busca esta credencial:
```
832922517843-21fdfg0s7h9qnl5kj6ip2vro3j4g8rvv.apps.googleusercontent.com
```

#### 3. Haz clic en el NOMBRE (no en el icono) para editarlo

#### 4. Busca la sección "URIs de redirección autorizados"

#### 5. Haz clic en "AGREGAR URI"

#### 6. Agrega EXACTAMENTE estas URIs (una por una):

```
http://localhost:8000/accounts/google/login/callback/
```

```
http://127.0.0.1:8000/accounts/google/login/callback/
```

⚠️ **IMPORTANTE:** 
- ✅ Debe tener `http://` (NO https)
- ✅ Debe terminar con `/` (barra final)
- ✅ Sin espacios
- ✅ Exactamente como está escrito

#### 7. Haz clic en "GUARDAR" (botón azul abajo)

#### 8. ESPERA 1-2 MINUTOS
Los cambios tardan un poco en propagarse en los servidores de Google.

#### 9. Cierra tu navegador o usa MODO INCÓGNITO

#### 10. Intenta de nuevo:
1. Ve a: http://127.0.0.1:8000/usuarios/login/
2. Haz clic en "Continuar con Google"
3. Selecciona tu cuenta: davidcristancho160@gmail.com

---

## 📸 CÓMO SE VE EN GOOGLE CLOUD CONSOLE

Deberías ver algo así:

```
URIs de redirección autorizados

✓ http://localhost:8000/accounts/google/login/callback/
✓ http://127.0.0.1:8000/accounts/google/login/callback/

[+ AGREGAR URI]

                                    [CANCELAR]  [GUARDAR]
```

---

## 🔍 VERIFICACIÓN

Después de agregar las URIs y guardar, verifica:

1. ✅ Las URIs están guardadas (refresca la página para confirmar)
2. ✅ Has esperado 1-2 minutos
3. ✅ Estás usando modo incógnito o has limpiado las cookies

---

## 🐛 SI AÚN NO FUNCIONA

### Verifica que tu app de Google esté en modo correcto:

1. Ve a: https://console.cloud.google.com/apis/credentials/consent
2. Verifica el "Publishing status":
   - Si dice "Testing": Tu correo debe estar en "Test users"
   - Si dice "In production": Debería funcionar para cualquiera

### Si está en "Testing", agrega tu correo:

1. En la misma página (OAuth consent screen)
2. Busca "Test users"
3. Haz clic en "+ ADD USERS"
4. Agrega: `davidcristancho160@gmail.com`
5. Guarda

---

## 📋 CHECKLIST COMPLETO

- [ ] Ir a https://console.cloud.google.com/apis/credentials
- [ ] Buscar el Client ID: 832922517843-21fdfg0s7h9qnl5kj6ip2vro3j4g8rvv...
- [ ] Hacer clic para editar
- [ ] Agregar: `http://localhost:8000/accounts/google/login/callback/`
- [ ] Agregar: `http://127.0.0.1:8000/accounts/google/login/callback/`
- [ ] Hacer clic en GUARDAR
- [ ] Esperar 1-2 minutos
- [ ] Verificar que el correo esté en "Test users" (si está en Testing)
- [ ] Probar en modo incógnito

---

## ⚡ ATAJO RÁPIDO

Ejecuta este comando para ver la URI exacta:

```bash
python mostrar_uri_callback.py
```

---

## 🎯 RESUMEN

**El problema:** Google rechaza la solicitud porque la URI de callback no está autorizada.

**La solución:** Agregar las URIs en Google Cloud Console → Credentials → Tu OAuth Client ID → URIs de redirección autorizados.

**Las URIs necesarias:**
- `http://localhost:8000/accounts/google/login/callback/`
- `http://127.0.0.1:8000/accounts/google/login/callback/`

**¡Después de esto funcionará perfectamente!** 🚀

