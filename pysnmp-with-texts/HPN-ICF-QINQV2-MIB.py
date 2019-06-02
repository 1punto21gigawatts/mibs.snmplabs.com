#
# PySNMP MIB module HPN-ICF-QINQV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-QINQV2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, iso, Counter32, Counter64, Bits, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "iso", "Counter32", "Counter64", "Bits", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hpnicfQinQv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137))
hpnicfQinQv2.setRevisions(('2013-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfQinQv2.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfQinQv2.setLastUpdated('201303080000Z')
if mibBuilder.loadTexts: hpnicfQinQv2.setOrganization('')
if mibBuilder.loadTexts: hpnicfQinQv2.setContactInfo('')
if mibBuilder.loadTexts: hpnicfQinQv2.setDescription('802.1 QinQv2 MIB Version 1')
hpnicfQinQv2MibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1))
hpnicfQinQv2ScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1))
hpnicfQinQv2ServiceTPID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2ServiceTPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2ServiceTPID.setDescription('TPID globally configured for service VLAN tags. The global TPID value for service VLAN tags does not take effect on interfaces where hpnicfQinQIfServiceTPID is configured. By default, the global TPID for service VLAN tags is 0x8100.')
hpnicfQinQv2CustomerTPID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2CustomerTPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2CustomerTPID.setDescription('TPID globally configured for customer VLAN tags. The global TPID value for customer VLAN tags does not take effect on interfaces where hpnicfQinQIfCustomerTPID is configured. By default, the global TPID for customer VLAN tags is 0x8100.')
hpnicfQinQv2IfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2), )
if mibBuilder.loadTexts: hpnicfQinQv2IfCfgTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfCfgTable.setDescription('802.1 QinQ configuration table.')
hpnicfQinQv2IfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfQinQv2IfCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfCfgEntry.setDescription('802.1 QinQ configuration entries.')
hpnicfQinQv2IfState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2IfState.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfState.setDescription('802.1 QinQ functions on the port. The value is false by default.')
hpnicfQinQv2IfServiceTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2IfServiceTPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfServiceTPID.setDescription('Service TPID value on the port.')
hpnicfQinQv2IfCustomerTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2IfCustomerTPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfCustomerTPID.setDescription('Customer TPID value on the port.')
hpnicfQinQv2IfTransVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(512, 512)).setFixedLength(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfQinQv2IfTransVlanList.setStatus('current')
if mibBuilder.loadTexts: hpnicfQinQv2IfTransVlanList.setDescription('Transparent VLANs described as a bitmap. Each octet within this value specifies a set of eight VLANs. The first octet specifies VLANs 1 through 8. The second octet specifies VLANs 9 through 16, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN.')
mibBuilder.exportSymbols("HPN-ICF-QINQV2-MIB", hpnicfQinQv2IfCustomerTPID=hpnicfQinQv2IfCustomerTPID, hpnicfQinQv2IfState=hpnicfQinQv2IfState, hpnicfQinQv2MibObject=hpnicfQinQv2MibObject, hpnicfQinQv2IfCfgTable=hpnicfQinQv2IfCfgTable, hpnicfQinQv2ScalarObjects=hpnicfQinQv2ScalarObjects, PYSNMP_MODULE_ID=hpnicfQinQv2, hpnicfQinQv2=hpnicfQinQv2, hpnicfQinQv2IfCfgEntry=hpnicfQinQv2IfCfgEntry, hpnicfQinQv2ServiceTPID=hpnicfQinQv2ServiceTPID, hpnicfQinQv2IfServiceTPID=hpnicfQinQv2IfServiceTPID, hpnicfQinQv2IfTransVlanList=hpnicfQinQv2IfTransVlanList, hpnicfQinQv2CustomerTPID=hpnicfQinQv2CustomerTPID)