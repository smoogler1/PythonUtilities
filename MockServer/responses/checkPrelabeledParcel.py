#EMERGENCY_DELIVERY
#COURIER_DELIVERING
#MISSING_PARCEL
#PLACED_BY_CUSTOMER

body = """{"payload":\n
{"customerPhone":"888000002",\n
"senderPhone":"888000122",\n
"boxMachine":"XX-07",\n
"senderBoxMachine":null,\n
"size":"A",\n
"onDeliveryAmount":0.00,\n
"customerReference":"_to_XX-07_21_07_2021_11_35_23-PL",\n
"parcelCode":"632589897133532013600001",\n
"automaticReturn":false,\n
"returnAddressVO":null,\n
"targetAddressVO":null,\n
"bussinesCustomer":false,\n
"directParcel":false,\n
"payCode":0,\n
"openCode":356095,\n
"returnCode":0,\n
"carrier":null,\n
"carrierReference":"",\n
"customerDeliveringCode":0,\n
"id":227,\n
"status":"COURIER_DELIVERING",\n
"payForReturn":false,\n
"personalID":"",\n
"personalID2":null,\n
"supplierPhone":null,\n
"supplier":null,\n
"providerPhone":"",\n
"provider":"",\n
"customerSpecialReq":null,\n
"multipleParcelsId":null,\n
"multipleParcelsCount":null,\n
"initialPackCode":null,\n
"pickupWithoutLabel":false,\n
"collectionBarcode":null,\n
"sendingAmount":[{"size":"A","amount":0.00},{"size":"B","amount":0.00},{"size":"C","amount":0.00},{"size":"D","amount":0.00}],\n
"chargeForSending":null,\n
"carrierAcquirerPayCode":null,\n
"serviceName":"STANDARD",\n
"reservationDataVO":null,\n
"timestamp":"2021-07-21T09:38:00.314+00:00",\n
"parcelAttributes":[],\n
"multiCompPotentialUuid":null,\n
"multiCompPotentialSize":null,\n
"endOfWeekCollection":false,\n
"availablePM":true},\n
"status":"OK_WITH_RESPONSE"}\n"""

url = '/api/v1/backofficeparcel/checkPrelabeledParcel'