#
# PySNMP MIB module BAY-STACK-DHCP-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-DHCP-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, MibIdentifier, NotificationType, Counter64, Integer32, ObjectIdentity, ModuleIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "Counter64", "Integer32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Bits")
RowStatus, TextualConvention, DateAndTime, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString", "TruthValue", "MacAddress")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackDhcpSnoopingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 17))
bayStackDhcpSnoopingMib.setRevisions(('2014-03-20 00:00', '2013-10-11 00:00', '2013-07-25 00:00', '2013-07-09 00:00', '2013-04-18 00:00', '2013-03-21 00:00', '2012-05-28 00:00', '2010-11-18 00:00', '2010-10-05 00:00', '2009-09-23 00:00', '2009-04-01 00:00', '2009-03-30 00:00', '2009-03-26 00:00', '2008-10-30 00:00', '2008-06-02 00:00', '2006-06-23 00:00',))
if mibBuilder.loadTexts: bayStackDhcpSnoopingMib.setLastUpdated('201403200000Z')
if mibBuilder.loadTexts: bayStackDhcpSnoopingMib.setOrganization('Nortel Ltd.')
bsDhcpSnoopingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 17, 0))
bsDhcpSnoopingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 17, 1))
bsDhcpSnoopingScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1))
bsDhcpSnoopingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingEnabled.setStatus('current')
bsDhcpSnoopingOption82Enabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingOption82Enabled.setStatus('current')
bsDhcpSnoopingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2), )
if mibBuilder.loadTexts: bsDhcpSnoopingVlanTable.setStatus('current')
bsDhcpSnoopingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingVlanId"))
if mibBuilder.loadTexts: bsDhcpSnoopingVlanEntry.setStatus('current')
bsDhcpSnoopingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: bsDhcpSnoopingVlanId.setStatus('current')
bsDhcpSnoopingVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingVlanEnabled.setStatus('current')
bsDhcpSnoopingVlanOption82Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingVlanOption82Enabled.setStatus('current')
bsDhcpSnoopingIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3), )
if mibBuilder.loadTexts: bsDhcpSnoopingIfTable.setStatus('current')
bsDhcpSnoopingIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfIndex"))
if mibBuilder.loadTexts: bsDhcpSnoopingIfEntry.setStatus('current')
bsDhcpSnoopingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsDhcpSnoopingIfIndex.setStatus('current')
bsDhcpSnoopingIfTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingIfTrusted.setStatus('current')
bsDhcpSnoopingIfOption82SubscriberId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingIfOption82SubscriberId.setStatus('current')
bsDhcpSnoopingBindingTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4), )
if mibBuilder.loadTexts: bsDhcpSnoopingBindingTable.setStatus('current')
bsDhcpSnoopingBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1), ).setIndexNames((0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingVlanId"), (0, "BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingMacAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingBindingEntry.setStatus('current')
bsDhcpSnoopingBindingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: bsDhcpSnoopingBindingVlanId.setStatus('current')
bsDhcpSnoopingBindingMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: bsDhcpSnoopingBindingMacAddress.setStatus('current')
bsDhcpSnoopingBindingAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingAddressType.setStatus('current')
bsDhcpSnoopingBindingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingAddress.setStatus('current')
bsDhcpSnoopingBindingInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingInterface.setStatus('current')
bsDhcpSnoopingBindingLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingLeaseTime.setStatus('current')
bsDhcpSnoopingBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingRowStatus.setStatus('current')
bsDhcpSnoopingBindingTimeToExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingTimeToExpiry.setStatus('current')
bsDhcpSnoopingBindingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("learned", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsDhcpSnoopingBindingSource.setStatus('current')
bsDhcpSnoopingNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5))
bsDhcpSnoopingNotificationSourcePort = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 1), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsDhcpSnoopingNotificationSourcePort.setStatus('current')
bsDhcpSnoopingNotificationMsgType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("dhcpDiscover", 1), ("dhcpOffer", 2), ("dhcpRequest", 3), ("dhcpDecline", 4), ("dhcpAck", 5), ("dhcpNak", 6), ("dhcpRelease", 7), ("dhcpInform", 8), ("dhcpForceRenew", 9), ("dhcpLeaseQuery", 10), ("dhcpLeaseUnassigned", 11), ("dhcpLeaseUnknown", 12), ("dhcpLeaseActive", 13)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsDhcpSnoopingNotificationMsgType.setStatus('current')
bsDhcpSnoopingNotificationSourceMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 3), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsDhcpSnoopingNotificationSourceMACAddr.setStatus('current')
bsDhcpSnoopingNotificationClientMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsDhcpSnoopingNotificationClientMACAddr.setStatus('current')
bsDhcpSnoopingNotificationsBindingMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 5, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsDhcpSnoopingNotificationsBindingMacAddress.setStatus('current')
bsDhcpSnoopingBindingTableFull = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 1)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationClientMACAddr"))
if mibBuilder.loadTexts: bsDhcpSnoopingBindingTableFull.setStatus('current')
bsDhcpSnoopingTrap = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 2)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourcePort"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationMsgType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourceMACAddr"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationClientMACAddr"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfTrusted"))
if mibBuilder.loadTexts: bsDhcpSnoopingTrap.setStatus('current')
bsDhcpOption82MaxLengthExceeded = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 3))
if mibBuilder.loadTexts: bsDhcpOption82MaxLengthExceeded.setStatus('current')
bsDhcpSnoopingExtSaveEntryMACConflict = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 4)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryMACConflict.setStatus('current')
bsDhcpSnoopingExtSaveEntryInvalidInterface = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 5)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingInterface"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryInvalidInterface.setStatus('current')
bsDhcpSnoopingExtSaveEntryLeaseExpired = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 6)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryLeaseExpired.setStatus('current')
bsDhcpSnoopingExtSaveEntryParsingFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 7)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryParsingFailure.setStatus('current')
bsDhcpSnoopingExtSaveNTP = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 8))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveNTP.setStatus('current')
bsDhcpSnoopingExtSaveUSBSyncSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 9)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveUSBSyncSuccess.setStatus('current')
bsDhcpSnoopingExtSaveTFTPSyncSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 10)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTFTPSyncSuccess.setStatus('current')
bsDhcpSnoopingExtSaveUSBSyncFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 11)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveUSBSyncFailure.setStatus('current')
bsDhcpSnoopingExtSaveTFTPSyncFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 12)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTFTPSyncFailure.setStatus('current')
bsDhcpSnoopingExtSaveUSBRestoreSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 13)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveUSBRestoreSuccess.setStatus('current')
bsDhcpSnoopingExtSaveTFTPRestoreSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 14)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTFTPRestoreSuccess.setStatus('current')
bsDhcpSnoopingExtSaveUSBRestoreFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 15)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveUsbTargetUnit"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveUSBRestoreFailure.setStatus('current')
bsDhcpSnoopingExtSaveTFTPRestoreFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 16)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveTftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTFTPRestoreFailure.setStatus('current')
bsDhcpSnoopingExtSaveEntryInvalidVlan = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 17)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingBindingVlanId"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryInvalidVlan.setStatus('current')
bsDhcpSnoopingExtSaveSFTPSyncSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 18)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSFTPSyncSuccess.setStatus('current')
bsDhcpSnoopingExtSaveSFTPSyncFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 19)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSFTPSyncFailure.setStatus('current')
bsDhcpSnoopingExtSaveSFTPRestoreSuccess = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 20)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSFTPRestoreSuccess.setStatus('current')
bsDhcpSnoopingExtSaveSFTPRestoreFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 21)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddressType"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingExtSaveSftpServerAddress"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSFTPRestoreFailure.setStatus('current')
bsDhcpSnoopingExtSaveEntryIfTrustedConflict = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 22)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationsBindingMacAddress"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfTrusted"))
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEntryIfTrustedConflict.setStatus('current')
bsDhcpSnoopingStaticEntryMACConflict = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 17, 0, 23)).setObjects(("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingNotificationSourceMACAddr"), ("BAY-STACK-DHCP-SNOOPING-MIB", "bsDhcpSnoopingIfIndex"))
if mibBuilder.loadTexts: bsDhcpSnoopingStaticEntryMACConflict.setStatus('current')
bsDhcpSnoopingExtSave = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6))
bsDhcpSnoopingExtSaveEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveEnabled.setStatus('current')
bsDhcpSnoopingExtSaveLastSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveLastSyncTime.setStatus('current')
bsDhcpSnoopingExtSaveSyncFlag = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSyncFlag.setStatus('current')
bsDhcpSnoopingExtSaveFilename = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveFilename.setStatus('current')
bsDhcpSnoopingExtSaveTftpServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTftpServerAddressType.setStatus('current')
bsDhcpSnoopingExtSaveTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveTftpServerAddress.setStatus('current')
bsDhcpSnoopingExtSaveUsbTargetUnit = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveUsbTargetUnit.setStatus('current')
bsDhcpSnoopingExtSaveForceRestore = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveForceRestore.setStatus('current')
bsDhcpSnoopingExtSaveSftpServerAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 9), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSftpServerAddressType.setStatus('current')
bsDhcpSnoopingExtSaveSftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 17, 1, 6, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsDhcpSnoopingExtSaveSftpServerAddress.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-DHCP-SNOOPING-MIB", bsDhcpSnoopingVlanOption82Enabled=bsDhcpSnoopingVlanOption82Enabled, bsDhcpSnoopingIfIndex=bsDhcpSnoopingIfIndex, bsDhcpSnoopingBindingRowStatus=bsDhcpSnoopingBindingRowStatus, bsDhcpSnoopingNotificationClientMACAddr=bsDhcpSnoopingNotificationClientMACAddr, bsDhcpSnoopingExtSaveEntryInvalidVlan=bsDhcpSnoopingExtSaveEntryInvalidVlan, bsDhcpSnoopingExtSaveForceRestore=bsDhcpSnoopingExtSaveForceRestore, bsDhcpSnoopingStaticEntryMACConflict=bsDhcpSnoopingStaticEntryMACConflict, bsDhcpSnoopingExtSaveFilename=bsDhcpSnoopingExtSaveFilename, bsDhcpSnoopingBindingSource=bsDhcpSnoopingBindingSource, bsDhcpSnoopingBindingTable=bsDhcpSnoopingBindingTable, PYSNMP_MODULE_ID=bayStackDhcpSnoopingMib, bsDhcpSnoopingExtSaveLastSyncTime=bsDhcpSnoopingExtSaveLastSyncTime, bsDhcpSnoopingTrap=bsDhcpSnoopingTrap, bsDhcpSnoopingNotificationObjects=bsDhcpSnoopingNotificationObjects, bsDhcpSnoopingNotificationsBindingMacAddress=bsDhcpSnoopingNotificationsBindingMacAddress, bsDhcpSnoopingExtSaveTftpServerAddress=bsDhcpSnoopingExtSaveTftpServerAddress, bsDhcpSnoopingExtSaveEntryMACConflict=bsDhcpSnoopingExtSaveEntryMACConflict, bsDhcpSnoopingNotificationSourcePort=bsDhcpSnoopingNotificationSourcePort, bsDhcpSnoopingExtSaveUSBSyncSuccess=bsDhcpSnoopingExtSaveUSBSyncSuccess, bsDhcpSnoopingVlanEnabled=bsDhcpSnoopingVlanEnabled, bsDhcpSnoopingIfEntry=bsDhcpSnoopingIfEntry, bsDhcpSnoopingExtSaveSftpServerAddressType=bsDhcpSnoopingExtSaveSftpServerAddressType, bsDhcpSnoopingVlanEntry=bsDhcpSnoopingVlanEntry, bsDhcpSnoopingExtSaveUSBSyncFailure=bsDhcpSnoopingExtSaveUSBSyncFailure, bsDhcpSnoopingExtSaveEntryIfTrustedConflict=bsDhcpSnoopingExtSaveEntryIfTrustedConflict, bsDhcpSnoopingExtSaveTftpServerAddressType=bsDhcpSnoopingExtSaveTftpServerAddressType, bsDhcpSnoopingOption82Enabled=bsDhcpSnoopingOption82Enabled, bsDhcpSnoopingNotificationSourceMACAddr=bsDhcpSnoopingNotificationSourceMACAddr, bsDhcpSnoopingExtSaveEnabled=bsDhcpSnoopingExtSaveEnabled, bsDhcpSnoopingIfTable=bsDhcpSnoopingIfTable, bsDhcpSnoopingExtSaveEntryLeaseExpired=bsDhcpSnoopingExtSaveEntryLeaseExpired, bsDhcpSnoopingIfOption82SubscriberId=bsDhcpSnoopingIfOption82SubscriberId, bsDhcpSnoopingBindingLeaseTime=bsDhcpSnoopingBindingLeaseTime, bsDhcpSnoopingExtSaveTFTPRestoreFailure=bsDhcpSnoopingExtSaveTFTPRestoreFailure, bsDhcpSnoopingBindingAddress=bsDhcpSnoopingBindingAddress, bsDhcpSnoopingBindingMacAddress=bsDhcpSnoopingBindingMacAddress, bsDhcpSnoopingExtSaveSFTPSyncSuccess=bsDhcpSnoopingExtSaveSFTPSyncSuccess, bsDhcpSnoopingExtSaveUSBRestoreSuccess=bsDhcpSnoopingExtSaveUSBRestoreSuccess, bsDhcpSnoopingVlanId=bsDhcpSnoopingVlanId, bsDhcpSnoopingNotificationMsgType=bsDhcpSnoopingNotificationMsgType, bsDhcpSnoopingExtSaveTFTPSyncFailure=bsDhcpSnoopingExtSaveTFTPSyncFailure, bsDhcpSnoopingBindingVlanId=bsDhcpSnoopingBindingVlanId, bsDhcpSnoopingExtSaveTFTPRestoreSuccess=bsDhcpSnoopingExtSaveTFTPRestoreSuccess, bsDhcpSnoopingExtSaveTFTPSyncSuccess=bsDhcpSnoopingExtSaveTFTPSyncSuccess, bsDhcpSnoopingExtSaveSFTPSyncFailure=bsDhcpSnoopingExtSaveSFTPSyncFailure, bsDhcpSnoopingExtSave=bsDhcpSnoopingExtSave, bsDhcpSnoopingExtSaveNTP=bsDhcpSnoopingExtSaveNTP, bsDhcpSnoopingBindingAddressType=bsDhcpSnoopingBindingAddressType, bsDhcpSnoopingScalars=bsDhcpSnoopingScalars, bsDhcpSnoopingExtSaveUsbTargetUnit=bsDhcpSnoopingExtSaveUsbTargetUnit, bsDhcpSnoopingExtSaveSftpServerAddress=bsDhcpSnoopingExtSaveSftpServerAddress, bsDhcpSnoopingObjects=bsDhcpSnoopingObjects, bsDhcpSnoopingExtSaveEntryInvalidInterface=bsDhcpSnoopingExtSaveEntryInvalidInterface, bsDhcpSnoopingBindingEntry=bsDhcpSnoopingBindingEntry, bsDhcpSnoopingExtSaveSFTPRestoreFailure=bsDhcpSnoopingExtSaveSFTPRestoreFailure, bsDhcpSnoopingExtSaveEntryParsingFailure=bsDhcpSnoopingExtSaveEntryParsingFailure, bsDhcpSnoopingBindingInterface=bsDhcpSnoopingBindingInterface, bsDhcpSnoopingNotifications=bsDhcpSnoopingNotifications, bsDhcpSnoopingBindingTimeToExpiry=bsDhcpSnoopingBindingTimeToExpiry, bsDhcpSnoopingBindingTableFull=bsDhcpSnoopingBindingTableFull, bsDhcpSnoopingVlanTable=bsDhcpSnoopingVlanTable, bsDhcpSnoopingExtSaveSyncFlag=bsDhcpSnoopingExtSaveSyncFlag, bsDhcpSnoopingExtSaveUSBRestoreFailure=bsDhcpSnoopingExtSaveUSBRestoreFailure, bsDhcpSnoopingExtSaveSFTPRestoreSuccess=bsDhcpSnoopingExtSaveSFTPRestoreSuccess, bsDhcpOption82MaxLengthExceeded=bsDhcpOption82MaxLengthExceeded, bsDhcpSnoopingEnabled=bsDhcpSnoopingEnabled, bsDhcpSnoopingIfTrusted=bsDhcpSnoopingIfTrusted, bayStackDhcpSnoopingMib=bayStackDhcpSnoopingMib)