#
# PySNMP MIB module GUDEADS-PDU8110-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GUDEADS-PDU8110-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, Counter64, ObjectIdentity, MibIdentifier, enterprises, Integer32, IpAddress, Bits, iso, ModuleIdentity, Counter32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "MibIdentifier", "enterprises", "Integer32", "IpAddress", "Bits", "iso", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gudeads = ModuleIdentity((1, 3, 6, 1, 4, 1, 28507))
gudeads.setRevisions(('2007-03-05 13:56',))
if mibBuilder.loadTexts: gudeads.setLastUpdated('200703051356Z')
if mibBuilder.loadTexts: gudeads.setOrganization('Gude Analog- und Digitalsysteme GmbH')
pdu8110PowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: pdu8110PowerIndex.setStatus('current')
pdu8110Current = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 5), Unsigned32()).setUnits('mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdu8110Current.setStatus('current')
pdu8110PowerTable = MibTable((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2), )
if mibBuilder.loadTexts: pdu8110PowerTable.setStatus('current')
pdu8110PowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1), ).setIndexNames((0, "GUDEADS-PDU8110-MIB", "pdu8110PowerIndex"))
if mibBuilder.loadTexts: pdu8110PowerEntry.setStatus('current')
pdu8110PowerChan = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1))
pdu8110ChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdu8110ChanStatus.setStatus('current')
pdu8110ActivePowerChan = MibScalar((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdu8110ActivePowerChan.setStatus('current')
events = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 0))
pdu8110TrapIPTable = MibTable((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2), )
if mibBuilder.loadTexts: pdu8110TrapIPTable.setStatus('current')
gadsPDU8110 = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23))
pdu8110TrapIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1), ).setIndexNames((0, "GUDEADS-PDU8110-MIB", "pdu8110TrapIPIndex"))
if mibBuilder.loadTexts: pdu8110TrapIPEntry.setStatus('current')
pdu8110TrapIPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: pdu8110TrapIPIndex.setStatus('current')
pdu8110DeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 2))
pdu8110ExtActors = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 4))
pdu8110ExtSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6))
pdu8110SensorTable = MibTable((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1), )
if mibBuilder.loadTexts: pdu8110SensorTable.setStatus('current')
pdu8110SensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1), ).setIndexNames((0, "GUDEADS-PDU8110-MIB", "pdu8110SensorIndex"))
if mibBuilder.loadTexts: pdu8110SensorEntry.setStatus('current')
pdu8110SensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: pdu8110SensorIndex.setStatus('current')
pdu8110TempSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 2), Integer32()).setUnits('0.1 degree Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdu8110TempSensor.setStatus('current')
pdu8110HygroSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 3), Integer32()).setUnits('0.1 percent humidity').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdu8110HygroSensor.setStatus('current')
pdu8110SNMPaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1))
pdu8110TrapCtrl = MibScalar((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdu8110TrapCtrl.setStatus('current')
pdu8110Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1))
pdu8110CommonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1))
pdu8110IntActors = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 3))
pdu8110TrapAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdu8110TrapAddr.setStatus('current')
pdu8110IntSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 1, 5))
pdu8110Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 2))
pdu8110Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 2, 1))
pdu8110Compls = MibIdentifier((1, 3, 6, 1, 4, 1, 28507, 23, 2, 2))
pdu8110TempEvtSen1 = NotificationType((1, 3, 6, 1, 4, 1, 28507, 23, 0, 1)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110TempSensor"))
if mibBuilder.loadTexts: pdu8110TempEvtSen1.setStatus('current')
pdu8110TempEvtSen2 = NotificationType((1, 3, 6, 1, 4, 1, 28507, 23, 0, 2)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110TempSensor"))
if mibBuilder.loadTexts: pdu8110TempEvtSen2.setStatus('current')
pdu8110HygroEvtSen1 = NotificationType((1, 3, 6, 1, 4, 1, 28507, 23, 0, 3)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor"))
if mibBuilder.loadTexts: pdu8110HygroEvtSen1.setStatus('current')
pdu8110HygroEvtSen2 = NotificationType((1, 3, 6, 1, 4, 1, 28507, 23, 0, 4)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor"))
if mibBuilder.loadTexts: pdu8110HygroEvtSen2.setStatus('current')
pdu8110BasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28507, 23, 2, 1, 1)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110TrapCtrl"), ("GUDEADS-PDU8110-MIB", "pdu8110TrapAddr"), ("GUDEADS-PDU8110-MIB", "pdu8110ActivePowerChan"), ("GUDEADS-PDU8110-MIB", "pdu8110ChanStatus"), ("GUDEADS-PDU8110-MIB", "pdu8110Current"), ("GUDEADS-PDU8110-MIB", "pdu8110TempSensor"), ("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdu8110BasicGroup = pdu8110BasicGroup.setStatus('current')
pdu8110NotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 28507, 23, 2, 1, 2)).setObjects(("GUDEADS-PDU8110-MIB", "pdu8110TempEvtSen1"), ("GUDEADS-PDU8110-MIB", "pdu8110TempEvtSen2"), ("GUDEADS-PDU8110-MIB", "pdu8110HygroEvtSen1"), ("GUDEADS-PDU8110-MIB", "pdu8110HygroEvtSen2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdu8110NotificationGroup = pdu8110NotificationGroup.setStatus('current')
mibBuilder.exportSymbols("GUDEADS-PDU8110-MIB", pdu8110NotificationGroup=pdu8110NotificationGroup, pdu8110HygroEvtSen2=pdu8110HygroEvtSen2, pdu8110ActivePowerChan=pdu8110ActivePowerChan, PYSNMP_MODULE_ID=gudeads, pdu8110TempEvtSen1=pdu8110TempEvtSen1, gadsPDU8110=gadsPDU8110, pdu8110SensorEntry=pdu8110SensorEntry, pdu8110IntActors=pdu8110IntActors, pdu8110SNMPaccess=pdu8110SNMPaccess, pdu8110TrapAddr=pdu8110TrapAddr, pdu8110PowerChan=pdu8110PowerChan, gudeads=gudeads, pdu8110HygroSensor=pdu8110HygroSensor, pdu8110Groups=pdu8110Groups, pdu8110ChanStatus=pdu8110ChanStatus, pdu8110Current=pdu8110Current, pdu8110DeviceConfig=pdu8110DeviceConfig, pdu8110TrapIPEntry=pdu8110TrapIPEntry, pdu8110PowerEntry=pdu8110PowerEntry, pdu8110TrapIPIndex=pdu8110TrapIPIndex, pdu8110IntSensors=pdu8110IntSensors, pdu8110HygroEvtSen1=pdu8110HygroEvtSen1, pdu8110SensorIndex=pdu8110SensorIndex, pdu8110TrapCtrl=pdu8110TrapCtrl, pdu8110TrapIPTable=pdu8110TrapIPTable, pdu8110Compls=pdu8110Compls, pdu8110ExtActors=pdu8110ExtActors, pdu8110SensorTable=pdu8110SensorTable, pdu8110CommonConfig=pdu8110CommonConfig, pdu8110TempSensor=pdu8110TempSensor, pdu8110BasicGroup=pdu8110BasicGroup, pdu8110Conf=pdu8110Conf, events=events, pdu8110TempEvtSen2=pdu8110TempEvtSen2, pdu8110PowerIndex=pdu8110PowerIndex, pdu8110PowerTable=pdu8110PowerTable, pdu8110Objects=pdu8110Objects, pdu8110ExtSensors=pdu8110ExtSensors)