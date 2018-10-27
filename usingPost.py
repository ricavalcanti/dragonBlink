import requests
import json
import time

# parametros
serial = "TEST02271018"
email = "rodolfo@email.com"
kVol = "sensorVolume1"
kCond = "sensorCond1"
kTemp = "sensorTemp1"
jsonLogin = {"email": email,
             "password": "12345678910", "serial": serial}
urlLogin = 'http://api.saiot.ect.ufrn.br/v1/device/auth/login'
urlCadastro = 'http://api.saiot.ect.ufrn.br/v1/device/manager/device'
urlHist = 'http://api.saiot.ect.ufrn.br/v1/device/history/logs'
broker = "api.saiot.ect.ufrn.br"
# pickup token
r = requests.post(urlLogin, json=jsonLogin)
token = r.text
print(token)
# cadastro device
jsonDevice = {"token":
              token,
              "data": {
                  "name": "SmartOrdenha",
                  "serial": serial,
                  "controllers": [],
                  "sensors": [
                      {
                          "key": kVol,
                          "tag": "Leite Produzido",
                          "unit": "Litros",
                          "type": "number"
                      },
                      {
                          "key": kCond,
                          "tag": "Condutância",
                          "unit": "miliSiemens/cm",
                          "type": "number"
                      },
                      {
                          "key": kTemp,
                          "tag": "Temperatura",
                          "unit": "°C",
                          "type": "number"
                      }
                  ]
              }
              }

retornoCadastro = requests.post(urlCadastro, json=jsonDevice)
print("Retorno do cadastro: " + retornoCadastro.text)


def sendData(dVolume, dTemp, dCond,dateTime):
    jsonReport = {
        "token": token,
        "data": [{
            "data": [{
                "serial": serial,
                kVol: dVolume,
                kCond : dCond,
                kTemp: dTemp
            }],
            "dateTime": dateTime
        }]
    }
    retornoData = requests.post(urlHist, json=jsonReport)
    print(retornoData.text)

sendData(20,28,5.3,"2018-10-26 09:51:52.220")