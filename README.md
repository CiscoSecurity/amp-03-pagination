[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### AMP for Endpoints pagination:

This script has the basic logic required for handling pagination in the AMP for Endpoints API. It simply prints the connector GUID and hostname to the console. It is using the default limit of 500, if you do not have more than 500 connectors in your environment no pagination will occur.

### Before using you must update the following:
- client_id 
- api_key

### Usage:
```
python 01_paginate.py
```

### Example script output:  
```
43ea5bb6-a4ec-48fa-876c-59cc304fda17 Demo_AMP
b0a69c58-be3a-4549-9c60-1d2fa3031229 Demo_AMP_Exploit_Prevention
14dcfce3-9663-434d-9beb-c8836de035ce Demo_AMP_Intel
43af918c-dc5e-4a64-ad17-63772c695e64 Demo_AMP_Threat_Quarantined
9fc87138-e65a-48cf-85c2-f5b8834e2109 Demo_Command_Line_Arguments_Kovter
d2721a44-3795-4138-a73a-f36e6d8b0201 Demo_Command_Line_Arguments_Meterpreter
884e8273-7665-4c02-a8a8-9e421d54bcbc Demo_CozyDuke
29c714f7-fc1e-4ecc-8178-1bca4630a587 Demo_CryptoWall
3949c60f-3389-4f76-989d-78d9f9758517 Demo_Cta
68e09992-0f55-4e4c-b1c5-de9a406dd6a9 Demo_Dridex
08dd0e8c-74fa-4cd6-bc98-fd687927d54d Demo_Dyre
d6ee5717-e019-4d23-b0ea-0d060245c9d3 Demo_iOS_1
64b20a4a-798a-439d-8a9a-a2ae92e782ee Demo_iOS_2
2e0ba8fd-64d4-4931-9fbc-b3d7d10edebe Demo_iOS_3
c5630b96-279b-4a86-b785-039b3a38ce67 Demo_iOS_4
e84077df-3e34-46c8-bc52-2c4354011961 Demo_iOS_5
cbd4b4fb-3fe0-4a9f-a079-0830773d8d43 Demo_Low_Prev_Retro
8c4e62cb-307d-4758-a976-4abcb9dcc809 Demo_Plugx
0ca4dfbf-34a9-49b0-aff6-e7d335aa3f01 Demo_Qakbot_1
1ac4325e-813a-440a-93c1-70b83bff153c Demo_Qakbot_2
5d0c9ee6-a7cc-4c36-84f3-b63b7c452050 Demo_Qakbot_3
34e1141e-4cab-4694-bf1d-cedb54b25af3 Demo_Ramnit
8c29fd99-f2e1-44cd-9d01-18737f97db9a Demo_SFEicar
a689cc25-a215-44a0-8ab5-7341465f38d7 Demo_Stabuniq
71e40cfc-6d75-4f8e-ad0f-fa5f330f0304 Demo_TDSS
6dc4849c-34ae-46c3-b6d7-79f24d4ae306 Demo_TeslaCrypt
696d4f1c-ce81-4097-ae5b-27fa57c55ca3 Demo_Tinba
b23f9bac-5249-424d-8b30-f6f4eb990399 Demo_Upatre
b4c142b9-0b48-4e11-9938-023751686d41 Demo_WannaCry_Ransomware
b65f26d5-d801-40e1-956c-f9854fa39cf4 Demo_ZAccess
81f698df-0510-46ee-a7a4-5e1098774f3b Demo_Zbot
```
