#
# PySNMP MIB module FDRY-IP-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-IP-SOURCE-GUARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, ModuleIdentity, ObjectIdentity, iso, Counter64, Integer32, Unsigned32, Bits, Gauge32, Counter32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Integer32", "Unsigned32", "Bits", "Gauge32", "Counter32", "MibIdentifier", "NotificationType")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
fdryIpSrcGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37))
fdryIpSrcGuardMIB.setRevisions(('2010-07-26 00:00', '2010-02-22 00:00',))
if mibBuilder.loadTexts: fdryIpSrcGuardMIB.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: fdryIpSrcGuardMIB.setOrganization('Brocade Communications Systems, Inc.')
class BindMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("active", 2), ("inactive", 3))

class BindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("ip", 2))

fdryIpSrcGuardInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1))
fdryIpSrcGuardPortVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2))
fdryIpSrcGuardBind = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3))
fdryIpSrcGuardIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardIfConfigTable.setStatus('current')
fdryIpSrcGuardIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fdryIpSrcGuardIfConfigEntry.setStatus('current')
fdryIpSrcGuardIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpSrcGuardIfEnable.setStatus('current')
fdryIpSrcGuardPortVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanConfigTable.setStatus('current')
fdryIpSrcGuardPortVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1), ).setIndexNames((0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanPortId"), (0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanVlanId"))
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanConfigEntry.setStatus('current')
fdryIpSrcGuardPortVlanPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanPortId.setStatus('current')
fdryIpSrcGuardPortVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 2), VlanIndex())
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanVlanId.setStatus('current')
fdryIpSrcGuardPortVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fdryIpSrcGuardPortVlanEnable.setStatus('current')
fdryIpSrcGuardBindTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1), )
if mibBuilder.loadTexts: fdryIpSrcGuardBindTable.setStatus('current')
fdryIpSrcGuardBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardBindIpAddr"))
if mibBuilder.loadTexts: fdryIpSrcGuardBindEntry.setStatus('current')
fdryIpSrcGuardBindIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: fdryIpSrcGuardBindIpAddr.setStatus('current')
fdryIpSrcGuardBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpSrcGuardBindVlanId.setStatus('current')
fdryIpSrcGuardBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpSrcGuardBindRowStatus.setStatus('current')
fdryIpSrcGuardBindMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 4), BindMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryIpSrcGuardBindMode.setStatus('current')
fdryIpSrcGuardBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 5), BindType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fdryIpSrcGuardBindType.setStatus('current')
mibBuilder.exportSymbols("FDRY-IP-SOURCE-GUARD-MIB", fdryIpSrcGuardPortVlanConfigEntry=fdryIpSrcGuardPortVlanConfigEntry, fdryIpSrcGuardPortVlanPortId=fdryIpSrcGuardPortVlanPortId, fdryIpSrcGuardBindMode=fdryIpSrcGuardBindMode, fdryIpSrcGuardPortVlanEnable=fdryIpSrcGuardPortVlanEnable, fdryIpSrcGuardInterface=fdryIpSrcGuardInterface, fdryIpSrcGuardBindTable=fdryIpSrcGuardBindTable, fdryIpSrcGuardBindRowStatus=fdryIpSrcGuardBindRowStatus, BindType=BindType, fdryIpSrcGuardBindType=fdryIpSrcGuardBindType, fdryIpSrcGuardBind=fdryIpSrcGuardBind, fdryIpSrcGuardBindEntry=fdryIpSrcGuardBindEntry, fdryIpSrcGuardBindIpAddr=fdryIpSrcGuardBindIpAddr, fdryIpSrcGuardIfConfigTable=fdryIpSrcGuardIfConfigTable, fdryIpSrcGuardIfEnable=fdryIpSrcGuardIfEnable, PYSNMP_MODULE_ID=fdryIpSrcGuardMIB, fdryIpSrcGuardMIB=fdryIpSrcGuardMIB, fdryIpSrcGuardPortVlanVlanId=fdryIpSrcGuardPortVlanVlanId, BindMode=BindMode, fdryIpSrcGuardPortVlanConfigTable=fdryIpSrcGuardPortVlanConfigTable, fdryIpSrcGuardBindVlanId=fdryIpSrcGuardBindVlanId, fdryIpSrcGuardPortVlan=fdryIpSrcGuardPortVlan, fdryIpSrcGuardIfConfigEntry=fdryIpSrcGuardIfConfigEntry)