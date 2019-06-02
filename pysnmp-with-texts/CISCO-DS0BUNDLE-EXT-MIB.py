#
# PySNMP MIB module CISCO-DS0BUNDLE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DS0BUNDLE-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:56:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dsx0BundleEntry, = mibBuilder.importSymbols("CISCO-DS0BUNDLE-MIB", "dsx0BundleEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, Integer32, Unsigned32, NotificationType, MibIdentifier, TimeTicks, Counter64, iso, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "iso", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDs0BundleExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 33))
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setLastUpdated('9806300000Z')
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setOrganization('Cisco Systems')
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setContactInfo(' Cisco Systems, Inc. 170 West Tasman Drive, San Jose CA 95134-1706. Phone: +1 408 526 5260 Email: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setDescription('The MIB module for managing DS0 Bundles. This MIB contains additional objects to supplement the the IETF draft ds0Bundle MIB.')
ciscoDs0BundleExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1))
cdsx0BundleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1))
cdsx0BundleInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2))
class Ds0ChannelList(TextualConvention, OctetString):
    description = 'A list of ds0 timeslots on a DS1 line. The list is specified as an OCTET STRING in which each ds0 timeslot is represented by a single bit, where timeslots 1 through 8 are represented by the bits in the first octet, timeslots 9 through 16 by the bits in the second octet, etc. In each octet, the lowest numbered timeslot is represented by the most significant bit, and the highest numbered timeslot by the least significant bit. A timeslot is present in the list when its bit is set, and absent when its bit is reset. If the OCTET STRING value has fewer bits than required to represent one or more timeslots on a DS1, then those timeslots are absent from the list. If the OCTET STRING value has more bits than required to represent the timeslots on a DS1, then the extra bits are ignored. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

cdsx0BundleExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1), )
if mibBuilder.loadTexts: cdsx0BundleExtTable.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtTable.setDescription('This table is used to supplement the dsx0BundleTable.')
cdsx0BundleExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1), )
dsx0BundleEntry.registerAugmentions(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtEntry"))
cdsx0BundleExtEntry.setIndexNames(*dsx0BundleEntry.getIndexNames())
if mibBuilder.loadTexts: cdsx0BundleExtEntry.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtEntry.setDescription('Contains objects to configure a ds0Bundle. The values of objects cdsx0BundleExtDs1Index and cdsx0BundleExtChannelMap must be specified for the associated row to become active.')
cdsx0BundleExtDs1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtDs1Index.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtDs1Index.setDescription('The ifIndex of the DS1 line containing the ds0 timeslots in this bundle. The ds0 bundle interface is layered on top of the DS1 line. This layering is represented in the ifStackTable. This object is not instantiated until the value is specified. The value may be set only when the ds0 bundle is created.')
cdsx0BundleExtChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 2), Ds0ChannelList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtChannelMap.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtChannelMap.setDescription('A list of ds0 timeslots that comprise this ds0 bundle. This object is not instantiated until the value is specified. The value may be set only when the ds0 bundle is created.')
cdsx0BundleExtEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("atmFuni", 2), ("frameRelay", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtEncapType.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtEncapType.setDescription('The type of encapsulation for this bundle. A ds0 bundle is a logical serial port. Setting this object defines the type of the serial port. If not specified, the value is none(1), indicating that the encapsulation type on this serial port is not defined. If the value is changed to atmFuni(2), the agent will create an entry in the ifTable with ifType equal to atmFuni(106). If the value is changed to frameRelay(3), the agent will create an entry in the ifTable with ifType equal to frameRelayService(44). The new atmFuni or frameRelayService interface is layered on top of the ds0 bundle interface. This layering will be represented in the ifStackTable. The value of this object can be changed only if the ifOperStatus of the associated atmFuni or frameRelayService interface is down. When the value is changed, the agent removes all existing connections on the interface, and also deletes the ifEntry that was created because of the previous value.')
cdsx0BundleExtChannelRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rate56", 1), ("rate64", 2))).clone('rate64')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtChannelRate.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleExtChannelRate.setDescription("The data rate of each ds0 in this bundle. rate56 - 56kb/s rate64 - 64kb/s For ds0's on a T1 line, the value should be rate56(1) if 'robbed bit' signaling is used, and rate64(2) if clear channel signaling is used. For ds0's on a E1 line, the value should always be rate64(2). The value can be set only when the entry is created.")
cdsx0BundleUseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1), )
if mibBuilder.loadTexts: cdsx0BundleUseTable.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleUseTable.setDescription('Shows the ds0 timeslots that are currently in use (i.e., part of a ds0 bundle) on channelized DS1 lines. There is an entry in this table for each channelized DS1 line which has an ifEntry.')
cdsx0BundleUseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdsx0BundleUseEntry.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleUseEntry.setDescription('Contains the ds0 timeslots that are currently part of various ds0 bundles on the DS1 line identified by the ifIndex. This information can be useful for an NMS when creating new ds0 bundles on this DS1.')
cdsx0BundleUseDs0Used = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1, 1), Ds0ChannelList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdsx0BundleUseDs0Used.setStatus('current')
if mibBuilder.loadTexts: cdsx0BundleUseDs0Used.setDescription('A list of ds0 timeslots on this DS1 line that are currently in use, i.e., are part of some ds0 bundle.')
ciscoDs0BundleExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3))
ciscoDs0BundleExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1))
ciscoDs0BundleExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2))
ciscoDs0BundleExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1, 1)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "ciscoDs0BundleExtConfigGroup"), ("CISCO-DS0BUNDLE-EXT-MIB", "ciscoDs0BundleExtInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtMIBCompliance = ciscoDs0BundleExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDs0BundleExtMIBCompliance.setDescription('The compliance statement for DS0Bundle interfaces.')
ciscoDs0BundleExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 1)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtDs1Index"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelMap"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtEncapType"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtConfigGroup = ciscoDs0BundleExtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDs0BundleExtConfigGroup.setDescription('A collection of objects providing the ability to configure a ds0 bundle.')
ciscoDs0BundleExtInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 2)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleUseDs0Used"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtInfoGroup = ciscoDs0BundleExtInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDs0BundleExtInfoGroup.setDescription('A collection of objects providing information about which ds0 timeslots are in ds0 bundles.')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-EXT-MIB", cdsx0BundleExtChannelMap=cdsx0BundleExtChannelMap, ciscoDs0BundleExtConfigGroup=ciscoDs0BundleExtConfigGroup, PYSNMP_MODULE_ID=ciscoDs0BundleExtMIB, cdsx0BundleInfo=cdsx0BundleInfo, cdsx0BundleUseEntry=cdsx0BundleUseEntry, cdsx0BundleConfig=cdsx0BundleConfig, cdsx0BundleExtTable=cdsx0BundleExtTable, cdsx0BundleExtEntry=cdsx0BundleExtEntry, cdsx0BundleExtEncapType=cdsx0BundleExtEncapType, cdsx0BundleUseTable=cdsx0BundleUseTable, Ds0ChannelList=Ds0ChannelList, ciscoDs0BundleExtMIBGroups=ciscoDs0BundleExtMIBGroups, ciscoDs0BundleExtMIBCompliances=ciscoDs0BundleExtMIBCompliances, cdsx0BundleUseDs0Used=cdsx0BundleUseDs0Used, ciscoDs0BundleExtMIB=ciscoDs0BundleExtMIB, cdsx0BundleExtChannelRate=cdsx0BundleExtChannelRate, ciscoDs0BundleExtMIBObjects=ciscoDs0BundleExtMIBObjects, cdsx0BundleExtDs1Index=cdsx0BundleExtDs1Index, ciscoDs0BundleExtMIBConformance=ciscoDs0BundleExtMIBConformance, ciscoDs0BundleExtMIBCompliance=ciscoDs0BundleExtMIBCompliance, ciscoDs0BundleExtInfoGroup=ciscoDs0BundleExtInfoGroup)