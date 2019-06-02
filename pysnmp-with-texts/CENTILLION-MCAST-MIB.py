#
# PySNMP MIB module CENTILLION-MCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-MCAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
EnableIndicator, PortId, sysConfig, StatusIndicator, Boolean, CardId = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "EnableIndicator", "PortId", "sysConfig", "StatusIndicator", "Boolean", "CardId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, NotificationType, MibIdentifier, Bits, ModuleIdentity, Integer32, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "IpAddress", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

vlan = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31))
vlanMcastProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1))
vlanIGMPProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1))
vlanIGMPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1))
igmpGeneralConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1), )
if mibBuilder.loadTexts: igmpGeneralConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigTable.setDescription('IP IGMP general configuration table which includes pseudo query, IRAP query configuration, and maximum number of groups supported in this VLAN.')
igmpGeneralConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpGeneralConfigVlanId"))
if mibBuilder.loadTexts: igmpGeneralConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigEntry.setDescription('IP IGMP general configuration entry. Each entry is indexed by a vlan id. An example to create the entry is: set igmpGeneralConfigIgmpSupport.3=I2 and igmpGeneralConfigMaxGroup.3=I20 to a switch ip address. (where 3 is vlan Id; 2 is enabled; 20 is maximum multicast groups to be supported for this vlan. ')
igmpGeneralConfigVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGeneralConfigVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigVlanId.setDescription('The unique VLAN identifier of this IGMP configuration entry. ')
igmpGeneralConfigPseudoQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 2), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigPseudoQuery.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigPseudoQuery.setDescription('In the absence of a true IGMP router, the switch may be configured to issue general queries. This provides the capability for multicast pruning with an isoloated subnet. The mode defaults to disabled in a VLAN configured for IGMP support')
igmpGeneralConfigIrapQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 3), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigIrapQuery.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigIrapQuery.setDescription("Control whether IGMP Router Advertisement Protocol messages will be used to determine the existence of a router in a remote switch. Default is 'enabled'.")
igmpGeneralConfigIgmpSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 4), EnableIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigIgmpSupport.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigIgmpSupport.setDescription(" When 'enabled' is specified, it indicates that the IGMP is supported in this VLAN.")
igmpGeneralConfigMaxGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGeneralConfigMaxGroup.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGeneralConfigMaxGroup.setDescription(' The maximum number of multicast groups supported in this VLAN. If the VLAN supports only manually configured multicast groups, then the value of this field equals the length of the IGMP multicast group if the multicast group is an inclusive set. A value of 0 indicates that IGMP multicasting is not supported in this VLAN')
igmpTimerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2), )
if mibBuilder.loadTexts: igmpTimerConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigTable.setDescription('IP IGMP Multicast timer configuration table')
igmpTimerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpTimerConfigVlanId"))
if mibBuilder.loadTexts: igmpTimerConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigEntry.setDescription('IP IGMP Multicast timer configuration entry. Each entry is indexed by a vlan id. This entry will be created when the corresponding igmpGeneralConfigEntry is created. All the values of the mibs in this entry will be set to default at the time of creation. ')
igmpTimerConfigVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpTimerConfigVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigVlanId.setDescription('The unique VLAN identifier of this multicast timer configuration entry.')
igmpTimerConfigTimerRobustness = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 2), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigTimerRobustness.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigTimerRobustness.setDescription('The robustness variable for the multicast group. A value of zero indicates the default value should be taken. If the value specified is non-zero, it should be equal or greater than 2')
igmpTimerConfigQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 3), Integer32().clone(125)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigQueryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigQueryInterval.setDescription('The query interval configured for the multicast group. A value of zero indicates the default value should be used. The value should be less than 0xffff')
igmpTimerConfigQueryResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 2, 1, 4), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpTimerConfigQueryResponse.setStatus('mandatory')
if mibBuilder.loadTexts: igmpTimerConfigQueryResponse.setDescription('The response interval configured for the multicast group. A value of zero indicates the default value should be used. The value should be less than 0xffff. ')
igmpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3), )
if mibBuilder.loadTexts: igmpGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupTable.setDescription('IP IGMP Multicast group address configuration table. ')
igmpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpGroupVlanId"), (0, "CENTILLION-MCAST-MIB", "igmpGroupStatic"), (0, "CENTILLION-MCAST-MIB", "igmpGroupAddress"))
if mibBuilder.loadTexts: igmpGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupEntry.setDescription('IP IGMP Multicast group configuration entry. Each entry is indexed by igmpGroupVlanId, igmpGroupStatic, and igmpGroupAddress')
igmpGroupVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupVlanId.setDescription('The unique VLAN identifier of this IGMP multicast group address entry. ')
igmpGroupStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 2), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupStatic.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupStatic.setDescription(' Indicates whether the IGMP multicast group was created statically(TRUE) by a management entity, or dynamically learned')
igmpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupAddress.setDescription('The multicast group address(Class D). The range is from 224.0.0.0 to 239.255.255.255. The addresses from 224.0.0.0 to 224.0.0.255 are reserved IP multicast addresses.')
igmpGroupIncluded = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGroupIncluded.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupIncluded.setDescription("Indicates the multicast addresses are to be included or excluded from the group. Dynamic entries are always included and can not be modified, while static entries may be either included or excluded. For each VLAN, it only allows to configure either 'included' as static or 'excluded' as static. ")
igmpGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 3, 1, 5), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpGroupStatus.setStatus('mandatory')
if mibBuilder.loadTexts: igmpGroupStatus.setDescription("The status of this multicast group entry: 'valid' and 'invalid'. This object enables the user to add or delete this multicast group. Setting the status as 'valid' is to add the entry; otherwise as 'invalid' is to delete the entry. An example to create an multicast group entry is: set igmpGroupStatus.3.1.224.0.0.1= valid where 3: vlan id; 1: static; 224.0.0.1: multicast group IP address")
igmpRouterPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4), )
if mibBuilder.loadTexts: igmpRouterPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortTable.setDescription('IP IGMP Multicast router port table. It contains a list of the ports containing configured IGMP routers. These ports initialize the IPrDtag and IPmDtag for the group.')
igmpRouterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1), ).setIndexNames((0, "CENTILLION-MCAST-MIB", "igmpRouterPortVlanId"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortStatic"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortCard"), (0, "CENTILLION-MCAST-MIB", "igmpRouterPortPort"))
if mibBuilder.loadTexts: igmpRouterPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortEntry.setDescription('IP IGMP Multicast router port entry. Each entry is indexed by igmpRouterPortVlanId, igmpRouterPortStatic, igmpRouterPortCard, igmpRouterPortPort')
igmpRouterPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortVlanId.setDescription('The unique VLAN identifier of this IGMP multicast router port entry. ')
igmpRouterPortStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 2), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortStatic.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortStatic.setDescription(' Indicates whether the IGMP multicast router port was created statically(TRUE) by a management entity, or dynamically learned. ')
igmpRouterPortCard = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 3), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortCard.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortCard.setDescription('The card id of this multicast router port entry. ')
igmpRouterPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 4), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpRouterPortPort.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortPort.setDescription('The port id of this multicast router port entry. ')
igmpRouterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 1, 1, 1, 4, 1, 5), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: igmpRouterPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: igmpRouterPortStatus.setDescription("The status of this multicast router port entry: 'valid' and 'invalid'. This object enables the user to add or delete this multicast group. Setting the status as 'valid' is to add the entry; otherwise as 'invalid' is to delete the entry. An example to create an multicast router port entry is: set igmpRouterPortStatus.3.1.5.2 = valid where 3: vlan id; 1: static; 5.2 : card/port that is connected with igmp router")
mibBuilder.exportSymbols("CENTILLION-MCAST-MIB", igmpGeneralConfigMaxGroup=igmpGeneralConfigMaxGroup, vlanMcastProtocolGroup=vlanMcastProtocolGroup, igmpTimerConfigVlanId=igmpTimerConfigVlanId, igmpRouterPortPort=igmpRouterPortPort, igmpGroupTable=igmpGroupTable, igmpGeneralConfigIgmpSupport=igmpGeneralConfigIgmpSupport, vlanIGMPProtocolGroup=vlanIGMPProtocolGroup, igmpRouterPortStatic=igmpRouterPortStatic, igmpGeneralConfigVlanId=igmpGeneralConfigVlanId, igmpGeneralConfigEntry=igmpGeneralConfigEntry, igmpRouterPortEntry=igmpRouterPortEntry, igmpGroupIncluded=igmpGroupIncluded, igmpGeneralConfigTable=igmpGeneralConfigTable, vlanIGMPConfig=vlanIGMPConfig, igmpRouterPortStatus=igmpRouterPortStatus, igmpGroupStatic=igmpGroupStatic, igmpTimerConfigTimerRobustness=igmpTimerConfigTimerRobustness, VlanId=VlanId, igmpTimerConfigQueryResponse=igmpTimerConfigQueryResponse, igmpGeneralConfigIrapQuery=igmpGeneralConfigIrapQuery, vlan=vlan, igmpGeneralConfigPseudoQuery=igmpGeneralConfigPseudoQuery, igmpTimerConfigTable=igmpTimerConfigTable, igmpGroupStatus=igmpGroupStatus, igmpGroupVlanId=igmpGroupVlanId, igmpGroupEntry=igmpGroupEntry, igmpTimerConfigEntry=igmpTimerConfigEntry, igmpRouterPortVlanId=igmpRouterPortVlanId, igmpGroupAddress=igmpGroupAddress, igmpRouterPortTable=igmpRouterPortTable, igmpTimerConfigQueryInterval=igmpTimerConfigQueryInterval, igmpRouterPortCard=igmpRouterPortCard)