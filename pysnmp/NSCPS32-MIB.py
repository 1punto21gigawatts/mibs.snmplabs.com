#
# PySNMP MIB module NSCPS32-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSCPS32-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
nsc, nscProducts = mibBuilder.importSymbols("NSC-MIB", "nsc", "nscProducts")
Party, = mibBuilder.importSymbols("RFC1353-MIB", "Party")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, ModuleIdentity, Bits, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Unsigned32, experimental, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ModuleIdentity", "Bits", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "experimental", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
nscHippiSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4))
ps32General = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1))
ps32SwitchDescr = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchDescr.setStatus('mandatory')
ps32SwitchVersion = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchVersion.setStatus('mandatory')
ps32SwitchDate = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32SwitchDate.setStatus('mandatory')
ps32SwitchTime = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32SwitchTime.setStatus('mandatory')
ps32SwitchAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("enable", 2), ("disable", 3), ("reset", 4), ("programload", 5), ("test", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32SwitchAdminStatus.setStatus('mandatory')
ps32SwitchOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 10))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("testing", 3), ("operational", 4), ("resetInProgress", 5), ("warning", 6), ("nonFatalError", 7), ("fatalError", 8), ("loading", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchOperStatus.setStatus('mandatory')
ps32SwitchPhysicalChanges = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchPhysicalChanges.setStatus('mandatory')
ps32SwitchDiagnosticReg = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchDiagnosticReg.setStatus('mandatory')
ps32SwitchMiscellanReg = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchMiscellanReg.setStatus('mandatory')
ps32SwitchDipSwitchReg = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SwitchDipSwitchReg.setStatus('mandatory')
ps32PowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2))
ps32NumPowerSupplies = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32NumPowerSupplies.setStatus('mandatory')
ps32PowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2), )
if mibBuilder.loadTexts: ps32PowerSupplyTable.setStatus('mandatory')
ps32PowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32PowerSupplyIndex"))
if mibBuilder.loadTexts: ps32PowerSupplyEntry.setStatus('mandatory')
ps32PowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyIndex.setStatus('mandatory')
ps32PowerSupplyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyDescr.setStatus('mandatory')
ps32PowerSupplyAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PowerSupplyAdminStatus.setStatus('mandatory')
ps32PowerSupplyOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 1), ("empty", 2), ("disabled", 3), ("bad", 4), ("warning", 5), ("standby", 6), ("engaged", 7), ("redundant", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyOperStatus.setStatus('mandatory')
ps32PowerSupplyHealthText = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyHealthText.setStatus('mandatory')
ps32PowerSupplyWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyWarnings.setStatus('mandatory')
ps32PowerSupplyFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerSupplyFailures.setStatus('mandatory')
ps32NumPowerOutputs = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32NumPowerOutputs.setStatus('mandatory')
ps32PowerOutputTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4), )
if mibBuilder.loadTexts: ps32PowerOutputTable.setStatus('mandatory')
ps32PowerOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32PowerSupplyIndex"), (0, "NSCPS32-MIB", "ps32PowerOutputIndex"))
if mibBuilder.loadTexts: ps32PowerOutputEntry.setStatus('mandatory')
ps32PowerOutputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputIndex.setStatus('mandatory')
ps32PowerOutputStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("bad", 2), ("warning", 3), ("good", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputStatus.setStatus('mandatory')
ps32PowerOutputNominalVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputNominalVoltage.setStatus('mandatory')
ps32PowerOutputOfferedVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputOfferedVoltage.setStatus('mandatory')
ps32PowerOutputWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputWarnings.setStatus('mandatory')
ps32PowerOutputFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PowerOutputFailures.setStatus('mandatory')
ps32Environ = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3))
ps32NumEnvironmentSensors = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32NumEnvironmentSensors.setStatus('mandatory')
ps32EnvironTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2), )
if mibBuilder.loadTexts: ps32EnvironTable.setStatus('mandatory')
ps32EnvironEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32EnvironIndex"))
if mibBuilder.loadTexts: ps32EnvironEntry.setStatus('mandatory')
ps32EnvironIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironIndex.setStatus('mandatory')
ps32EnvironSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("logicovertemp", 2), ("fanfailure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironSensor.setStatus('mandatory')
ps32EnvironStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("bad", 2), ("warning", 3), ("good", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironStatus.setStatus('mandatory')
ps32EnvironWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironWarnings.setStatus('mandatory')
ps32EnvironFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironFailures.setStatus('mandatory')
ps32EnvironDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironDescriptor.setStatus('mandatory')
ps32EnvironHealthText = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 3, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32EnvironHealthText.setStatus('mandatory')
ps32Slot = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4))
ps32NumSlots = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32NumSlots.setStatus('mandatory')
ps32SlotTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2), )
if mibBuilder.loadTexts: ps32SlotTable.setStatus('mandatory')
ps32SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32SlotNumber"))
if mibBuilder.loadTexts: ps32SlotEntry.setStatus('mandatory')
ps32SlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SlotNumber.setStatus('mandatory')
ps32SlotPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SlotPartNumber.setStatus('mandatory')
ps32SlotBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SlotBoardID.setStatus('mandatory')
ps32SlotBoardText = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SlotBoardText.setStatus('mandatory')
ps32SlotLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 4, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32SlotLastChange.setStatus('mandatory')
ps32Port = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5))
ps32MaximumPorts = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32MaximumPorts.setStatus('mandatory')
ps32InstalledPorts = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32InstalledPorts.setStatus('mandatory')
ps32PortTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3), )
if mibBuilder.loadTexts: ps32PortTable.setStatus('mandatory')
ps32PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32PortNumber"))
if mibBuilder.loadTexts: ps32PortEntry.setStatus('mandatory')
ps32PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortNumber.setStatus('mandatory')
ps32PortBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortBoard.setStatus('mandatory')
ps32PortInput = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortInput.setStatus('mandatory')
ps32PortOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortOutput.setStatus('mandatory')
ps32PortForce = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortForce.setStatus('mandatory')
ps32PortCounterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortCounterStatus.setStatus('mandatory')
ps32PortOverrunCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortOverrunCount.setStatus('mandatory')
ps32PortSwitchRejectCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortSwitchRejectCount.setStatus('mandatory')
ps32PortCamponDelayCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortCamponDelayCount.setStatus('mandatory')
ps32PortCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortCurrentStatus.setStatus('mandatory')
ps32PortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("enable", 2), ("disable", 3), ("reset", 4), ("test", 5), ("clrerrors", 6), ("clrpaths", 7), ("clrstats", 8), ("clrall", 9), ("rstrpath", 10), ("savecfg", 11), ("savepath", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PortAdminStatus.setStatus('mandatory')
ps32PortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 5, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("notinstalled", 2), ("disabled", 3), ("operational", 4), ("connected", 5), ("intest", 6), ("inerror", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PortOperStatus.setStatus('mandatory')
ps32Pathway = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6))
ps32MaximumPathways = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32MaximumPathways.setStatus('mandatory')
ps32PathwayTable = MibTable((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2), )
if mibBuilder.loadTexts: ps32PathwayTable.setStatus('mandatory')
ps32PathwayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1), ).setIndexNames((0, "NSCPS32-MIB", "ps32PathwayPortNumber"), (0, "NSCPS32-MIB", "ps32PathwayHDA"))
if mibBuilder.loadTexts: ps32PathwayEntry.setStatus('mandatory')
ps32PathwayPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PathwayPortNumber.setStatus('mandatory')
ps32PathwayHDA = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 2), PhysAddress().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ps32PathwayHDA.setStatus('mandatory')
ps32PathwayDest = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PathwayDest.setStatus('mandatory')
ps32PathwayClear = MibTableColumn((1, 3, 6, 1, 4, 1, 10, 2, 1, 4, 6, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ps32PathwayClear.setStatus('mandatory')
mibBuilder.exportSymbols("NSCPS32-MIB", ps32PortOperStatus=ps32PortOperStatus, ps32PowerSupply=ps32PowerSupply, ps32SlotEntry=ps32SlotEntry, ps32PathwayHDA=ps32PathwayHDA, ps32EnvironStatus=ps32EnvironStatus, ps32PowerSupplyDescr=ps32PowerSupplyDescr, ps32NumSlots=ps32NumSlots, ps32PathwayDest=ps32PathwayDest, ps32SwitchDipSwitchReg=ps32SwitchDipSwitchReg, ps32PortCounterStatus=ps32PortCounterStatus, ps32MaximumPathways=ps32MaximumPathways, ps32SlotBoardText=ps32SlotBoardText, ps32PortAdminStatus=ps32PortAdminStatus, ps32General=ps32General, ps32PortForce=ps32PortForce, ps32PowerOutputNominalVoltage=ps32PowerOutputNominalVoltage, ps32PowerOutputTable=ps32PowerOutputTable, ps32NumEnvironmentSensors=ps32NumEnvironmentSensors, ps32SwitchPhysicalChanges=ps32SwitchPhysicalChanges, ps32SwitchTime=ps32SwitchTime, ps32PowerOutputWarnings=ps32PowerOutputWarnings, ps32Slot=ps32Slot, ps32PowerOutputFailures=ps32PowerOutputFailures, ps32SlotPartNumber=ps32SlotPartNumber, ps32PortOverrunCount=ps32PortOverrunCount, ps32PowerOutputEntry=ps32PowerOutputEntry, ps32PowerSupplyOperStatus=ps32PowerSupplyOperStatus, ps32Port=ps32Port, ps32PortEntry=ps32PortEntry, ps32PowerOutputOfferedVoltage=ps32PowerOutputOfferedVoltage, ps32EnvironTable=ps32EnvironTable, ps32Pathway=ps32Pathway, ps32NumPowerOutputs=ps32NumPowerOutputs, ps32SwitchVersion=ps32SwitchVersion, ps32PathwayTable=ps32PathwayTable, ps32SlotNumber=ps32SlotNumber, ps32SlotLastChange=ps32SlotLastChange, ps32SlotBoardID=ps32SlotBoardID, ps32PortOutput=ps32PortOutput, ps32PowerOutputIndex=ps32PowerOutputIndex, ps32SwitchMiscellanReg=ps32SwitchMiscellanReg, ps32PortBoard=ps32PortBoard, ps32PowerSupplyFailures=ps32PowerSupplyFailures, ps32EnvironFailures=ps32EnvironFailures, ps32EnvironDescriptor=ps32EnvironDescriptor, ps32PortTable=ps32PortTable, ps32SwitchOperStatus=ps32SwitchOperStatus, ps32MaximumPorts=ps32MaximumPorts, ps32PowerSupplyTable=ps32PowerSupplyTable, ps32InstalledPorts=ps32InstalledPorts, ps32EnvironWarnings=ps32EnvironWarnings, ps32PowerSupplyIndex=ps32PowerSupplyIndex, ps32SwitchDiagnosticReg=ps32SwitchDiagnosticReg, ps32PowerSupplyWarnings=ps32PowerSupplyWarnings, ps32EnvironIndex=ps32EnvironIndex, ps32SlotTable=ps32SlotTable, ps32PowerSupplyAdminStatus=ps32PowerSupplyAdminStatus, ps32PowerOutputStatus=ps32PowerOutputStatus, ps32SwitchDate=ps32SwitchDate, ps32EnvironEntry=ps32EnvironEntry, ps32PortInput=ps32PortInput, ps32PathwayPortNumber=ps32PathwayPortNumber, ps32SwitchDescr=ps32SwitchDescr, ps32SwitchAdminStatus=ps32SwitchAdminStatus, ps32EnvironSensor=ps32EnvironSensor, ps32PortSwitchRejectCount=ps32PortSwitchRejectCount, ps32PathwayClear=ps32PathwayClear, nscHippiSwitch=nscHippiSwitch, ps32Environ=ps32Environ, ps32PowerSupplyHealthText=ps32PowerSupplyHealthText, ps32PortCamponDelayCount=ps32PortCamponDelayCount, ps32PortNumber=ps32PortNumber, ps32PathwayEntry=ps32PathwayEntry, ps32PortCurrentStatus=ps32PortCurrentStatus, ps32NumPowerSupplies=ps32NumPowerSupplies, ps32PowerSupplyEntry=ps32PowerSupplyEntry, ps32EnvironHealthText=ps32EnvironHealthText)