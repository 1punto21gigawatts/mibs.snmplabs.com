#
# PySNMP MIB module CYCLADES-ACS-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-PM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, IpAddress, Gauge32, Integer32, ObjectIdentity, Bits, Counter32, TimeTicks, Unsigned32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "IpAddress", "Gauge32", "Integer32", "ObjectIdentity", "Bits", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 5))
cyPM.setRevisions(('2005-08-29 00:00', '2003-10-17 00:00',))
if mibBuilder.loadTexts: cyPM.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyPM.setOrganization('Cyclades Corporation')
cyNumberOfPM = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyNumberOfPM.setStatus('current')
cyPMTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2), )
if mibBuilder.loadTexts: cyPMTable.setStatus('current')
cyPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"))
if mibBuilder.loadTexts: cyPMEntry.setStatus('current')
cyPMSerialPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMSerialPortNumber.setStatus('current')
cyPMNumberOutlets = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMNumberOutlets.setStatus('current')
cyPMNumberUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMNumberUnits.setStatus('current')
cyPMCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMCurrent.setStatus('current')
cyPMVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMVersion.setStatus('current')
cyPMTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMTemperature.setStatus('current')
cyPMCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyPMCommand.setStatus('current')
cyPMUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3), )
if mibBuilder.loadTexts: cyPMUnitTable.setStatus('current')
cyPMUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"), (0, "CYCLADES-ACS-PM-MIB", "cyPMUnitNumber"))
if mibBuilder.loadTexts: cyPMUnitEntry.setStatus('current')
cyPMUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cyPMUnitNumber.setStatus('current')
cyPMUnitVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitVersion.setStatus('current')
cyPMUnitOutlets = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitOutlets.setStatus('current')
cyPMUnitFirstOutlet = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitFirstOutlet.setStatus('current')
cyPMUnitCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitCurrent.setStatus('current')
cyPMUnitMaxCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitMaxCurrent.setStatus('current')
cyPMUnitTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyPMUnitTemperature.setStatus('current')
cyPMUnitMaxTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 3, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyPMUnitMaxTemperature.setStatus('current')
cyOutletTable = MibTable((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4), )
if mibBuilder.loadTexts: cyOutletTable.setStatus('current')
cyOutletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1), ).setIndexNames((0, "CYCLADES-ACS-PM-MIB", "cyPMSerialPortNumber"), (0, "CYCLADES-ACS-PM-MIB", "cyOutletNumber"))
if mibBuilder.loadTexts: cyOutletEntry.setStatus('current')
cyOutletNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cyOutletNumber.setStatus('current')
cyOutletName = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletName.setStatus('current')
cyOutletServer = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyOutletServer.setStatus('current')
cyOutletPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2), ("unknow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletPower.setStatus('current')
cyOutletLock = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unlock", 0), ("lock", 1), ("unknow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletLock.setStatus('current')
cyOutletPUInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2925, 4, 5, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyOutletPUInterval.setStatus('current')
mibBuilder.exportSymbols("CYCLADES-ACS-PM-MIB", cyOutletName=cyOutletName, cyPMUnitMaxTemperature=cyPMUnitMaxTemperature, cyPMUnitNumber=cyPMUnitNumber, cyPMCommand=cyPMCommand, cyPMNumberUnits=cyPMNumberUnits, cyPM=cyPM, cyPMEntry=cyPMEntry, PYSNMP_MODULE_ID=cyPM, cyPMUnitMaxCurrent=cyPMUnitMaxCurrent, cyOutletEntry=cyOutletEntry, cyOutletNumber=cyOutletNumber, cyPMUnitVersion=cyPMUnitVersion, cyPMVersion=cyPMVersion, cyOutletTable=cyOutletTable, cyPMTable=cyPMTable, cyOutletServer=cyOutletServer, cyOutletLock=cyOutletLock, cyPMTemperature=cyPMTemperature, cyPMUnitEntry=cyPMUnitEntry, cyPMUnitFirstOutlet=cyPMUnitFirstOutlet, cyPMUnitTable=cyPMUnitTable, cyPMUnitTemperature=cyPMUnitTemperature, cyPMUnitCurrent=cyPMUnitCurrent, cyOutletPower=cyOutletPower, cyPMUnitOutlets=cyPMUnitOutlets, cyPMCurrent=cyPMCurrent, cyOutletPUInterval=cyOutletPUInterval, cyNumberOfPM=cyNumberOfPM, cyPMSerialPortNumber=cyPMSerialPortNumber, cyPMNumberOutlets=cyPMNumberOutlets)