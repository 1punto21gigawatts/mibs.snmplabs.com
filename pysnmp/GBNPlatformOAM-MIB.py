#
# PySNMP MIB module GBNPlatformOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNPlatformOAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
gbnPlatform, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnPlatform")
dot1qStaticMulticastEntry, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qStaticMulticastEntry", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Counter32, Unsigned32, IpAddress, iso, TimeTicks, MibIdentifier, NotificationType, Bits, Gauge32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Counter32", "Unsigned32", "IpAddress", "iso", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "Gauge32", "ModuleIdentity", "Counter64")
RowStatus, DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
gbnPlatformOAM = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1))
gbnPlatformOAM.setRevisions(('1900-11-02 00:00',))
if mibBuilder.loadTexts: gbnPlatformOAM.setLastUpdated('0011020000Z')
if mibBuilder.loadTexts: gbnPlatformOAM.setOrganization('Greentech')
class VctRunResultTxRxPairNoType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("txpair1", 0), ("rxpair1", 1), ("txpair2", 2), ("rxpair2", 3))

class VctRunResultStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("normal", 0), ("short", 1), ("open", 2), ("impedance_mismatch", 3))

gbnPlatformOAMSysIf = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1))
gbnPlatformOAMSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2))
gbnPlatformOAMIpAccessControl = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3))
gbnPlatformOAMWatchDog = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 4))
gbnPlatformOAMMuser = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5))
gbnPlatformOAMUpDownLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6))
gbnPlatformOAMSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7))
gbnPlatformOAMSntpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 8))
gbnPlatformOAMSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 9))
gbnPlatformOAMPortCar = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10))
gbnPlatformOAMSsh = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11))
gbnPlatformOAMMailalarm = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12))
gbnPlatformOAMVctRun = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13))
gbnPlatformOAMVctRunResult = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14))
sysIfMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfMACAddr.setStatus('current')
sysIfIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfIpAddress.setStatus('current')
sysIfIPGateAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfIPGateAddress.setStatus('current')
sysIfIPNetMask = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfIPNetMask.setStatus('current')
sysIfIPStatus = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notModified", 1), ("modified", 2), ("restore", 3), ("apply", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfIPStatus.setStatus('current')
sysIfBOOTPOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfBOOTPOnOff.setStatus('current')
sysIfDHCPOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfDHCPOnOff.setStatus('current')
sysIfManageVLANTbale = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9), )
if mibBuilder.loadTexts: sysIfManageVLANTbale.setStatus('mandatory')
sysIfManageVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "sysIfManageVLANVid"))
if mibBuilder.loadTexts: sysIfManageVLANEntry.setStatus('mandatory')
sysIfManageVLANVid = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysIfManageVLANVid.setStatus('current')
sysIfManageVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysIfManageVLANRowStatus.setStatus('current')
softwarePlate = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwarePlate.setStatus('current')
softwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareVersion.setStatus('current')
softwareCompiledTimeE = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareCompiledTimeE.setStatus('current')
softwareCompiledTimeC = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareCompiledTimeC.setStatus('current')
cpuDescription = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuDescription.setStatus('current')
sdramDescription = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdramDescription.setStatus('current')
flashDescription = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashDescription.setStatus('current')
hardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareVersion.setStatus('current')
bootromVersion = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootromVersion.setStatus('current')
hostName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostName.setStatus('current')
cpuIdle = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuIdle.setStatus('current')
memorySize = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memorySize.setStatus('current')
memoryIdle = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memoryIdle.setStatus('current')
systemClock = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14))
clockTime = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clockTime.setStatus('current')
timeZoneName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeZoneName.setStatus('current')
timeZoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86399))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeZoneOffset.setStatus('current')
offsetNegFlag = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 14, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: offsetNegFlag.setStatus('current')
productName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: productName.setStatus('current')
systemReset = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("reset", 2), ("resetToDefaults", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemReset.setStatus('current')
writeConfig = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noop", 1), ("save", 2), ("saveInProgress", 3), ("saveFailed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: writeConfig.setStatus('current')
saveNMInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18))
nmInterfaceId = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmInterfaceId.setStatus('current')
nmInterfaceIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmInterfaceIpAddress.setStatus('current')
nmInterfaceNetMask = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmInterfaceNetMask.setStatus('current')
nmInterfaceGateAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmInterfaceGateAddress.setStatus('current')
writeNMInterfaceConifig = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("saveNmconfig", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: writeNMInterfaceConifig.setStatus('current')
writeNMInterfaceConifigStatus = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 18, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("saveSuccess", 1), ("saveInProgress", 2), ("saveFailed", 3), ("noInterface", 4), ("noIpAddress", 5), ("differentSubnet", 6), ("noInterfaceParameter", 7), ("noIpAddressParameter", 8), ("noMaskParameter", 9), ("noGatewayParameter", 10), ("invalidIpOrMask", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: writeNMInterfaceConifigStatus.setStatus('current')
prodSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodSerialNo.setStatus('current')
cpuBusyStatus = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuBusyStatus.setStatus('current')
cpuBusyAlarmEnable = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 21), TruthValue().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuBusyAlarmEnable.setStatus('current')
cpuBusyThreshold = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuBusyThreshold.setStatus('current')
cpuUnbusyThreshold = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 23), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuUnbusyThreshold.setStatus('current')
cpuStatusTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24))
cpuBusyTrap = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24, 1))
if mibBuilder.loadTexts: cpuBusyTrap.setStatus('current')
cpuUnbusyTrap = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 2, 24, 2))
if mibBuilder.loadTexts: cpuUnbusyTrap.setStatus('current')
ipAccessControlTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: ipAccessControlTable.setStatus('current')
ipAccessControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "controlIpAddress"), (0, "GBNPlatformOAM-MIB", "controlIpMask"), (0, "GBNPlatformOAM-MIB", "controlTeminal"))
if mibBuilder.loadTexts: ipAccessControlEntry.setStatus('current')
controlIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlIpAddress.setStatus('current')
controlIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlIpMask.setStatus('current')
controlTeminal = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snmp", 1), ("web", 2), ("telnet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlTeminal.setStatus('current')
controlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("destroy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlStatus.setStatus('current')
softDogProxy = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softDogProxy.setStatus('current')
musrTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1), )
if mibBuilder.loadTexts: musrTable.setStatus('current')
musrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "musrIndex"))
if mibBuilder.loadTexts: musrEntry.setStatus('current')
musrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: musrIndex.setStatus('current')
musrName = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: musrName.setStatus('current')
musrPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: musrPassword.setStatus('current')
musrType = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normalUser", 0), ("superUser", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: musrType.setStatus('current')
musrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: musrRowStatus.setStatus('current')
manageUserAuthenType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("locacl", 1), ("radius", 2), ("radiusFailLocal", 3), ("tacacsplus", 4), ("tacacsplusFailLocal", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageUserAuthenType.setStatus('current')
manageUserAuthenRadiusName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageUserAuthenRadiusName.setStatus('current')
manageUserAuthChallegeType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chap", 1), ("pap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageUserAuthChallegeType.setStatus('current')
manageUserTacacsAuthor = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageUserTacacsAuthor.setStatus('current')
manageUserTacacsAccount = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 5, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manageUserTacacsAccount.setStatus('current')
loadTftpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadTftpAddress.setStatus('current')
loadTftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadTftpFileName.setStatus('current')
loadType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("application", 1), ("normalBootRom", 2), ("configuration", 3), ("bootCode", 4), ("alarm", 5), ("syslog", 6), ("wholeBootRom", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadType.setStatus('current')
loadExecute = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noop", 1), ("downloadTftp", 2), ("uploadTftp", 3), ("downloadFtp", 4), ("uploadFtp", 5), ("downloadXmodem", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadExecute.setStatus('current')
loadExecuteStatus = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("notStarted", 1), ("inProgressTftp", 2), ("successTftp", 3), ("errorConnectionTftp", 4), ("errorFilenameTftp", 5), ("errorFaultTftp", 6), ("inProgressFtp", 7), ("successFtp", 8), ("errorConnectionFtp", 9), ("errorFilenameFtp", 10), ("errorFaultFtp", 11), ("inProgressXmodem", 12), ("successXmodem", 13), ("errorConnectionXmodem", 14), ("errorFilenameXmodem", 15), ("errorFaultXmodem", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadExecuteStatus.setStatus('current')
loadFtpAddress = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadFtpAddress.setStatus('current')
loadFtpFileName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadFtpFileName.setStatus('current')
loadFtpUserName = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadFtpUserName.setStatus('current')
loadFtpUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 6, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: loadFtpUserPassword.setStatus('current')
snmpCommunityToViewTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1), )
if mibBuilder.loadTexts: snmpCommunityToViewTable.setStatus('current')
snmpCommunityToViewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "snmpComm2ViewIndex"))
if mibBuilder.loadTexts: snmpCommunityToViewEntry.setStatus('current')
snmpComm2ViewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: snmpComm2ViewIndex.setStatus('current')
snmpComm2ViewCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpComm2ViewCommName.setStatus('current')
snmpComm2ViewViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpComm2ViewViewName.setStatus('current')
snmpComm2ViewPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpComm2ViewPermission.setStatus('current')
snmpComm2ViewRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpComm2ViewRowStatus.setStatus('current')
snmpNotifyTypeTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2), )
if mibBuilder.loadTexts: snmpNotifyTypeTable.setStatus('current')
snmpNotifyTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "snmpPrivateNotifyType"))
if mibBuilder.loadTexts: snmpNotifyTypeEntry.setStatus('current')
snmpPrivateNotifyType = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpPrivateNotifyType.setStatus('current')
snmpNotifyTypeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpNotifyTypeStatus.setStatus('current')
gbnPlatformOAMSnmpNotifyType = MibIdentifier((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 3))
snmpNotifyTypeSaveConfiguration = NotificationType((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 3, 1))
if mibBuilder.loadTexts: snmpNotifyTypeSaveConfiguration.setStatus('current')
snmpTrapSource = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSource.setStatus('current')
snmpRemoteEngineTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5), )
if mibBuilder.loadTexts: snmpRemoteEngineTable.setStatus('current')
snmpRemoteEngineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "snmpRemoteEngineID"))
if mibBuilder.loadTexts: snmpRemoteEngineEntry.setStatus('current')
snmpRemoteEngineID = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 1), DisplayString())
if mibBuilder.loadTexts: snmpRemoteEngineID.setStatus('current')
snmpRemoteHostTAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpRemoteHostTAddr.setStatus('current')
snmpDeleteRemoteEngineTableRow = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteRow", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpDeleteRemoteEngineTableRow.setStatus('current')
snmpTrapSourceType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 7, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSourceType.setStatus('current')
portCarTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1), )
if mibBuilder.loadTexts: portCarTable.setStatus('current')
portCarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "portCarPort"))
if mibBuilder.loadTexts: portCarEntry.setStatus('current')
portCarPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: portCarPort.setStatus('current')
portCarEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portCarEnable.setStatus('current')
portDiscardBpdu = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portDiscardBpdu.setStatus('current')
portCarRateBpdu = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portCarRateBpdu.setStatus('current')
portCarGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portCarGlobalEnable.setStatus('current')
portCarOpenTime = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portCarOpenTime.setStatus('current')
discardBpdu = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: discardBpdu.setStatus('current')
portCarRate = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 10, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portCarRate.setStatus('current')
vctRunTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1), )
if mibBuilder.loadTexts: vctRunTable.setStatus('current')
vctRunEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "vctRunPort"))
if mibBuilder.loadTexts: vctRunEntry.setStatus('current')
vctRunPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: vctRunPort.setStatus('current')
vctRunEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vctRunEnable.setStatus('current')
vctAutoRunEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vctAutoRunEnable.setStatus('current')
vctAutoRunGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 13, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vctAutoRunGlobalEnable.setStatus('current')
vctRunResultTable = MibTable((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1), )
if mibBuilder.loadTexts: vctRunResultTable.setStatus('current')
vctRunResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1), ).setIndexNames((0, "GBNPlatformOAM-MIB", "vctRunResultPort"), (0, "GBNPlatformOAM-MIB", "vctRunResultTxRxPairNo"))
if mibBuilder.loadTexts: vctRunResultEntry.setStatus('current')
vctRunResultPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: vctRunResultPort.setStatus('current')
vctRunResultTxRxPairNo = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 2), VctRunResultTxRxPairNoType())
if mibBuilder.loadTexts: vctRunResultTxRxPairNo.setStatus('current')
vctRunResultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 3), VctRunResultStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vctRunResultStatus.setStatus('current')
vctRunResultErrorLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 14, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vctRunResultErrorLocation.setStatus('current')
mibBuilder.exportSymbols("GBNPlatformOAM-MIB", snmpNotifyTypeTable=snmpNotifyTypeTable, sysIfManageVLANVid=sysIfManageVLANVid, cpuStatusTrap=cpuStatusTrap, gbnPlatformOAMSnmpNotifyType=gbnPlatformOAMSnmpNotifyType, vctAutoRunEnable=vctAutoRunEnable, timeZoneName=timeZoneName, softwarePlate=softwarePlate, loadFtpUserPassword=loadFtpUserPassword, gbnPlatformOAMMuser=gbnPlatformOAMMuser, systemClock=systemClock, sysIfMACAddr=sysIfMACAddr, gbnPlatformOAMSntpClient=gbnPlatformOAMSntpClient, gbnPlatformOAMVctRunResult=gbnPlatformOAMVctRunResult, sdramDescription=sdramDescription, gbnPlatformOAMVctRun=gbnPlatformOAMVctRun, controlIpAddress=controlIpAddress, ipAccessControlTable=ipAccessControlTable, snmpNotifyTypeStatus=snmpNotifyTypeStatus, softwareCompiledTimeE=softwareCompiledTimeE, vctRunTable=vctRunTable, cpuIdle=cpuIdle, snmpComm2ViewViewName=snmpComm2ViewViewName, nmInterfaceIpAddress=nmInterfaceIpAddress, sysIfBOOTPOnOff=sysIfBOOTPOnOff, manageUserTacacsAuthor=manageUserTacacsAuthor, sysIfManageVLANTbale=sysIfManageVLANTbale, writeNMInterfaceConifigStatus=writeNMInterfaceConifigStatus, loadTftpFileName=loadTftpFileName, portCarOpenTime=portCarOpenTime, snmpTrapSource=snmpTrapSource, snmpRemoteEngineTable=snmpRemoteEngineTable, portCarEntry=portCarEntry, snmpTrapSourceType=snmpTrapSourceType, vctRunResultEntry=vctRunResultEntry, nmInterfaceGateAddress=nmInterfaceGateAddress, flashDescription=flashDescription, portCarTable=portCarTable, gbnPlatformOAMIpAccessControl=gbnPlatformOAMIpAccessControl, musrPassword=musrPassword, cpuUnbusyTrap=cpuUnbusyTrap, hardwareVersion=hardwareVersion, sysIfManageVLANEntry=sysIfManageVLANEntry, softwareCompiledTimeC=softwareCompiledTimeC, VctRunResultStatusType=VctRunResultStatusType, prodSerialNo=prodSerialNo, vctAutoRunGlobalEnable=vctAutoRunGlobalEnable, snmpComm2ViewCommName=snmpComm2ViewCommName, snmpComm2ViewPermission=snmpComm2ViewPermission, softDogProxy=softDogProxy, vctRunResultTxRxPairNo=vctRunResultTxRxPairNo, vctRunEnable=vctRunEnable, gbnPlatformOAMUpDownLoad=gbnPlatformOAMUpDownLoad, loadExecuteStatus=loadExecuteStatus, musrType=musrType, loadExecute=loadExecute, sysIfIPStatus=sysIfIPStatus, vctRunPort=vctRunPort, cpuDescription=cpuDescription, sysIfDHCPOnOff=sysIfDHCPOnOff, sysIfIPNetMask=sysIfIPNetMask, loadFtpAddress=loadFtpAddress, cpuBusyThreshold=cpuBusyThreshold, controlTeminal=controlTeminal, musrRowStatus=musrRowStatus, loadFtpFileName=loadFtpFileName, gbnPlatformOAMWatchDog=gbnPlatformOAMWatchDog, musrEntry=musrEntry, vctRunResultStatus=vctRunResultStatus, timeZoneOffset=timeZoneOffset, controlIpMask=controlIpMask, portCarRate=portCarRate, writeNMInterfaceConifig=writeNMInterfaceConifig, loadTftpAddress=loadTftpAddress, snmpRemoteEngineEntry=snmpRemoteEngineEntry, gbnPlatformOAMSystem=gbnPlatformOAMSystem, manageUserAuthenRadiusName=manageUserAuthenRadiusName, hostName=hostName, cpuBusyStatus=cpuBusyStatus, gbnPlatformOAMSsh=gbnPlatformOAMSsh, gbnPlatformOAMMailalarm=gbnPlatformOAMMailalarm, sysIfIpAddress=sysIfIpAddress, portCarRateBpdu=portCarRateBpdu, snmpNotifyTypeEntry=snmpNotifyTypeEntry, sysIfManageVLANRowStatus=sysIfManageVLANRowStatus, clockTime=clockTime, vctRunResultPort=vctRunResultPort, sysIfIPGateAddress=sysIfIPGateAddress, snmpComm2ViewIndex=snmpComm2ViewIndex, snmpNotifyTypeSaveConfiguration=snmpNotifyTypeSaveConfiguration, discardBpdu=discardBpdu, productName=productName, snmpDeleteRemoteEngineTableRow=snmpDeleteRemoteEngineTableRow, nmInterfaceId=nmInterfaceId, cpuBusyTrap=cpuBusyTrap, manageUserAuthenType=manageUserAuthenType, writeConfig=writeConfig, softwareVersion=softwareVersion, loadType=loadType, gbnPlatformOAMSyslog=gbnPlatformOAMSyslog, bootromVersion=bootromVersion, gbnPlatformOAMSnmp=gbnPlatformOAMSnmp, gbnPlatformOAMPortCar=gbnPlatformOAMPortCar, snmpCommunityToViewTable=snmpCommunityToViewTable, portCarPort=portCarPort, gbnPlatformOAMSysIf=gbnPlatformOAMSysIf, saveNMInterfaceConfig=saveNMInterfaceConfig, snmpRemoteHostTAddr=snmpRemoteHostTAddr, loadFtpUserName=loadFtpUserName, VctRunResultTxRxPairNoType=VctRunResultTxRxPairNoType, controlStatus=controlStatus, musrIndex=musrIndex, vctRunResultErrorLocation=vctRunResultErrorLocation, systemReset=systemReset, portDiscardBpdu=portDiscardBpdu, ipAccessControlEntry=ipAccessControlEntry, PYSNMP_MODULE_ID=gbnPlatformOAM, snmpComm2ViewRowStatus=snmpComm2ViewRowStatus, musrTable=musrTable, cpuBusyAlarmEnable=cpuBusyAlarmEnable, snmpCommunityToViewEntry=snmpCommunityToViewEntry, vctRunResultTable=vctRunResultTable, memoryIdle=memoryIdle, cpuUnbusyThreshold=cpuUnbusyThreshold, manageUserTacacsAccount=manageUserTacacsAccount, snmpPrivateNotifyType=snmpPrivateNotifyType, offsetNegFlag=offsetNegFlag, manageUserAuthChallegeType=manageUserAuthChallegeType, memorySize=memorySize, snmpRemoteEngineID=snmpRemoteEngineID, portCarEnable=portCarEnable, vctRunEntry=vctRunEntry, nmInterfaceNetMask=nmInterfaceNetMask, portCarGlobalEnable=portCarGlobalEnable, musrName=musrName, gbnPlatformOAM=gbnPlatformOAM)