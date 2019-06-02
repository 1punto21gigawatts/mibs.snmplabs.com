#
# PySNMP MIB module JUNIPER-L2ALD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-L2ALD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
jnxl2aldMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxl2aldMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, TimeTicks, Integer32, Counter32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ObjectIdentity, iso, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "TimeTicks", "Integer32", "Counter32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ObjectIdentity", "iso", "Counter64", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
jnxl2aldMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1))
jnxl2aldMib.setRevisions(('2015-01-22 10:00', '2015-01-14 10:00', '2012-08-08 10:00', '2007-02-15 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxl2aldMib.setRevisionsDescriptions(('Added a new field jnxL2aldVlanFdbId to the table jnxL2aldVlanTable', 'Added new table jnxL2aldVlanTable', 'Added new notification jnxl2aldMacMoveThreshold', 'Initial Version',))
if mibBuilder.loadTexts: jnxl2aldMib.setLastUpdated('201208081000Z')
if mibBuilder.loadTexts: jnxl2aldMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxl2aldMib.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxl2aldMib.setDescription('The MIB modules for L2ALD traps')
jnxl2aldNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0))
jnxl2aldObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1))
jnxl2aldInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1), )
if mibBuilder.loadTexts: jnxl2aldInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldInterfaceTable.setDescription('L2ALD objects for interface MAC limit.')
jnxl2aldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxl2aldEntry.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldEntry.setDescription('An entry in l2aldInterfaceTable.')
jnxl2aldIntfLogicalRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldIntfLogicalRouter.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldIntfLogicalRouter.setDescription('The logical router string for interface table.')
jnxl2aldIntfRoutingInst = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldIntfRoutingInst.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldIntfRoutingInst.setDescription('The routing instance string for interface table.')
jnxl2aldIntfBridgeDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldIntfBridgeDomain.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldIntfBridgeDomain.setDescription('The bridge domain string for interface table.')
jnxl2aldIntfMacLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldIntfMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldIntfMacLimit.setDescription('The MAC limit count for the interface table.')
jnxl2aldRoutingInst = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldRoutingInst.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldRoutingInst.setDescription('The Routing instance string for routing mac limit trap.')
jnxl2aldBridgeDomain = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldBridgeDomain.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldBridgeDomain.setDescription('The bridge domain string for routing mac limit trap.')
jnxl2aldLogicalRouter = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldLogicalRouter.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldLogicalRouter.setDescription('The logical router string for routing mac limit trap.')
jnxl2aldMacLimit = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldMacLimit.setDescription('The mac limit count for routing instance.')
jnxl2aldGbMacLimit = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 6), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldGbMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldGbMacLimit.setDescription('The mac limit count for the system.')
jnxl2aldMacAdress = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxl2aldMacAdress.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldMacAdress.setDescription('The offending mac causing mac move threshold trap.')
jnxL2aldMacNotificationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2))
jnxL2aldMacNotificationMIBGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1))
jnxL2aldMacGlobalFeatureEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacGlobalFeatureEnabled.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacGlobalFeatureEnabled.setDescription('Indicates whether the MAC notification feature is currently running in the device. Setting this object to false(2) disables the MAC notification feature globally. Setting this object to true(1) will start the MAC notification feature running in the device. If the feature is already running, setting to true(1) has no effect.')
jnxL2aldMacNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(30)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacNotificationInterval.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacNotificationInterval.setDescription('This object specifies the maximum interval of time between jnxL2aldMacChangedNotifications being generated by the device. If the value of jnxNotificationsEnabled is true(1), the device will send out the generated jnxL2aldMacChangedNotifications and archive the MAC change notification events in the jnxMacHistoryTable. If the value of jnxNotificationEnabled is false(2), the device will not send out the generated jnxL2aldMacChangedNotifications but it will archive these events in the jnxMacHistoryTable. If the value of this object is equal to 0, the device will generate jnxL2aldMacChangedNotifications and archive the MAC change notification events in the jnxMacHistoryTable as soon as there is MAC address learnt or removed by the device. If the value of this object is greater than 0, the device will wait for a period of time equal to the value of this object before generate the jnxL2aldMacChangedNotifications and archive the MAC change notification events in the jnxMacHistoryTable.')
jnxL2aldMacAddressesLearnt = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacAddressesLearnt.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacAddressesLearnt.setDescription('Indicates the number of MAC addresses learnt by the device.')
jnxL2aldMacAddressesRemoved = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacAddressesRemoved.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacAddressesRemoved.setDescription('Indicates the number of MAC addresses removed from the forwarding database.')
jnxL2aldMacNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacNotificationsEnabled.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacNotificationsEnabled.setDescription("Indicates whether jnxL2aldMacChangedNotification notifications will or will not be sent when there are MAC addresses learnt or removed from the device's forwarding database. Disabling notifications does not prevent the MAC address info from being added to the jnxMacHistoryTable.")
jnxL2aldMacNotificationsSent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacNotificationsSent.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacNotificationsSent.setDescription('Indicates the number of jnxl2aldMacChangedNotifications sent out by the device.')
jnxL2aldMacHistTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500)).clone(256)).setUnits('entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacHistTableMaxLength.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacHistTableMaxLength.setDescription('The upper limit on the number of entries that the jnxMacHistoryTable may contain. A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and a new one will be created.')
jnxL2aldMacHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8), )
if mibBuilder.loadTexts: jnxL2aldMacHistoryTable.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacHistoryTable.setDescription('This table will archive the MAC change notification events generated by this device. The MAC change notification events are archived here even if jnxMacChangesNotifications are not actually sent.')
jnxL2aldMacHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1), ).setIndexNames((0, "JUNIPER-L2ALD-MIB", "jnxL2aldHistIndex"))
if mibBuilder.loadTexts: jnxL2aldMacHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacHistoryEntry.setDescription('A MAC change notification message that was previously generated by this device. Each entry is indexed by a message index.')
jnxL2aldHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: jnxL2aldHistIndex.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldHistIndex.setDescription('An index that uniquely identifies a MAC change notification event previously generated by the device. This index starts at 1 and increases by one when a MAC change notification is generated. When it reaches the maximum value, the agent wraps the value back to 1.')
jnxL2aldHistMacChangedMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldHistMacChangedMsg.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldHistMacChangedMsg.setDescription("This object contains the information of a MAC change notification event. It consists of several tuples packed together in the format of '<tuple1><tuple2>...'. Each tuple consist of 13 octets in the format of '<operation><VLAN INDEX><MAC><dot1dBasePort><VLAN TAG>' where <operation> is of size 1 octet and supports the following values 0 - End of MIB object. 1 - MAC learnt. 2 - MAC removed. 3 - MAC updated. <VLAN INDEX> is the index of the VLAN which the MAC address is belonged to and has size of 2 octet. <MAC> is the Layer2 Mac Address and has size of 6 octets. <dot1dBasePort> is the value of dot1dBasePort for the interface from which the MAC address is learnt and has size of 2 octets. <VLAN TAG> is the tag of the VLAN which the MAC address is belonged to and has size of 2 octet.")
jnxL2aldHistTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 8, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldHistTimestamp.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldHistTimestamp.setDescription('The value of sysUpTime when the jnxL2aldMacChangedNotification containing the information denoted by the jnxHistMacChangedMsg object in this entry was generated.')
jnxL2aldMacAddressesUpdated = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldMacAddressesUpdated.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacAddressesUpdated.setDescription('Indicates the number of MAC addresses updated by the device.')
jnxL2aldVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3))
jnxL2aldVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1), )
if mibBuilder.loadTexts: jnxL2aldVlanTable.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanTable.setDescription('A table of VLAN names and characteristics.')
jnxL2aldVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1), ).setIndexNames((0, "JUNIPER-L2ALD-MIB", "jnxL2aldVlanID"))
if mibBuilder.loadTexts: jnxL2aldVlanEntry.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanEntry.setDescription('A table entry containing VLAN names and characteristics.')
jnxL2aldVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: jnxL2aldVlanID.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanID.setDescription('This is the locally significant ID that is used internally by this device to reference this VLAN.')
jnxL2aldVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldVlanName.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanName.setDescription('Vlan name is the textual name and this is the identifier that the user of a configuration utility will use.')
jnxL2aldVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldVlanTag.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanTag.setDescription('This is the locally significant ID that is used internally by this device to reference this VLAN.')
jnxL2aldVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldVlanType.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanType.setDescription('The vlan type can be Static (1) Dynamic(2)')
jnxL2aldVlanFdbId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxL2aldVlanFdbId.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldVlanFdbId.setDescription('The identity of the Filtering Database dot1qFdbTable (A table that contains configuration and control information for each Filtering Database currently operating on this device)')
jnxl2aldRoutingInstMacLimit = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 1)).setObjects(("JUNIPER-L2ALD-MIB", "jnxl2aldLogicalRouter"), ("JUNIPER-L2ALD-MIB", "jnxl2aldRoutingInst"), ("JUNIPER-L2ALD-MIB", "jnxl2aldBridgeDomain"), ("JUNIPER-L2ALD-MIB", "jnxl2aldMacLimit"))
if mibBuilder.loadTexts: jnxl2aldRoutingInstMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldRoutingInstMacLimit.setDescription('This notification is generated when the MAC limit for given routing instance (jnxl2aldRoutingInst) is reached. This trap is send only once we exceed the limit value.')
jnxl2aldInterfaceMacLimit = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 2)).setObjects(("JUNIPER-L2ALD-MIB", "jnxl2aldIntfLogicalRouter"), ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfRoutingInst"), ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfBridgeDomain"), ("IF-MIB", "ifDescr"), ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfMacLimit"))
if mibBuilder.loadTexts: jnxl2aldInterfaceMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldInterfaceMacLimit.setDescription('This notification is generated when the MAC limit for the given physical interface (jnxl2aldInterfaceMacLimit) is reached. This trap is send only once we exceed the limit value.')
jnxl2aldGlobalMacLimit = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 3)).setObjects(("JUNIPER-L2ALD-MIB", "jnxl2aldGbMacLimit"))
if mibBuilder.loadTexts: jnxl2aldGlobalMacLimit.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldGlobalMacLimit.setDescription('This notification is generated when the MAC limit for the entire system is reached. This trap is send only once we exceed the limit value.')
jnxl2aldMacMoveThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 4)).setObjects(("JUNIPER-L2ALD-MIB", "jnxl2aldIntfLogicalRouter"), ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfRoutingInst"), ("JUNIPER-L2ALD-MIB", "jnxl2aldIntfBridgeDomain"), ("IF-MIB", "ifDescr"), ("JUNIPER-L2ALD-MIB", "jnxl2aldMacAdress"))
if mibBuilder.loadTexts: jnxl2aldMacMoveThreshold.setStatus('current')
if mibBuilder.loadTexts: jnxl2aldMacMoveThreshold.setDescription('This notification is generated when a mac move reaches threshold. The given interface (ifDescr) will be blocked for the Bridge Domain(jnxl2aldIntfBridgeDomain). This trap is send only once when mac move count exceeds the threshold for the Mac(jnxl2aldMacAdress).')
jnxL2aldMacChangedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 48, 1, 0, 5)).setObjects(("JUNIPER-L2ALD-MIB", "jnxL2aldHistMacChangedMsg"), ("JUNIPER-L2ALD-MIB", "jnxL2aldHistTimestamp"))
if mibBuilder.loadTexts: jnxL2aldMacChangedNotification.setStatus('current')
if mibBuilder.loadTexts: jnxL2aldMacChangedNotification.setDescription('This notification is generated when there is enough MAC address information to fully occupy a maximum size SNMP trap message. This notification is also generated when there is at least one MAC address changed or removed and the amount of time elapsed from the previous notification is greater than the maximum wait time denoted by jnxNotificationInterval object. If there are more MAC addresses information than can fit into one cmmHistTrapContent object, then multiple notifications will be generated.')
mibBuilder.exportSymbols("JUNIPER-L2ALD-MIB", jnxl2aldIntfLogicalRouter=jnxl2aldIntfLogicalRouter, jnxL2aldVlanFdbId=jnxL2aldVlanFdbId, jnxl2aldIntfMacLimit=jnxl2aldIntfMacLimit, jnxL2aldMacChangedNotification=jnxL2aldMacChangedNotification, jnxL2aldMacAddressesLearnt=jnxL2aldMacAddressesLearnt, jnxL2aldMacAddressesUpdated=jnxL2aldMacAddressesUpdated, jnxL2aldHistTimestamp=jnxL2aldHistTimestamp, jnxL2aldHistMacChangedMsg=jnxL2aldHistMacChangedMsg, jnxl2aldIntfBridgeDomain=jnxl2aldIntfBridgeDomain, jnxl2aldObjects=jnxl2aldObjects, jnxl2aldLogicalRouter=jnxl2aldLogicalRouter, jnxl2aldEntry=jnxl2aldEntry, jnxl2aldInterfaceMacLimit=jnxl2aldInterfaceMacLimit, jnxl2aldMacLimit=jnxl2aldMacLimit, jnxL2aldMacNotificationMIBObjects=jnxL2aldMacNotificationMIBObjects, PYSNMP_MODULE_ID=jnxl2aldMib, jnxL2aldMacGlobalFeatureEnabled=jnxL2aldMacGlobalFeatureEnabled, jnxL2aldHistIndex=jnxL2aldHistIndex, jnxl2aldMib=jnxl2aldMib, jnxl2aldInterfaceTable=jnxl2aldInterfaceTable, jnxL2aldMacHistoryTable=jnxL2aldMacHistoryTable, jnxl2aldRoutingInstMacLimit=jnxl2aldRoutingInstMacLimit, jnxl2aldMacMoveThreshold=jnxl2aldMacMoveThreshold, jnxL2aldMacHistTableMaxLength=jnxL2aldMacHistTableMaxLength, jnxL2aldMacNotificationInterval=jnxL2aldMacNotificationInterval, jnxl2aldIntfRoutingInst=jnxl2aldIntfRoutingInst, jnxl2aldGbMacLimit=jnxl2aldGbMacLimit, jnxL2aldVlanMIBObjects=jnxL2aldVlanMIBObjects, jnxL2aldMacNotificationMIBGlobalObjects=jnxL2aldMacNotificationMIBGlobalObjects, jnxL2aldMacNotificationsSent=jnxL2aldMacNotificationsSent, jnxl2aldGlobalMacLimit=jnxl2aldGlobalMacLimit, jnxL2aldMacAddressesRemoved=jnxL2aldMacAddressesRemoved, jnxL2aldMacNotificationsEnabled=jnxL2aldMacNotificationsEnabled, jnxL2aldVlanName=jnxL2aldVlanName, jnxL2aldVlanType=jnxL2aldVlanType, jnxl2aldNotification=jnxl2aldNotification, jnxl2aldRoutingInst=jnxl2aldRoutingInst, jnxL2aldVlanID=jnxL2aldVlanID, jnxl2aldBridgeDomain=jnxl2aldBridgeDomain, jnxL2aldVlanTag=jnxL2aldVlanTag, jnxL2aldVlanEntry=jnxL2aldVlanEntry, jnxL2aldVlanTable=jnxL2aldVlanTable, jnxl2aldMacAdress=jnxl2aldMacAdress, jnxL2aldMacHistoryEntry=jnxL2aldMacHistoryEntry)