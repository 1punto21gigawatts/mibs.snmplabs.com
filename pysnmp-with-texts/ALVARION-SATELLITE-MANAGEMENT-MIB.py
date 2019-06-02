#
# PySNMP MIB module ALVARION-SATELLITE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-SATELLITE-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSIDOrNone, AlvarionNotificationEnable = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSIDOrNone", "AlvarionNotificationEnable")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Gauge32, Counter64, Counter32, ModuleIdentity, Integer32, IpAddress, Bits, NotificationType, TimeTicks, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Gauge32", "Counter64", "Counter32", "ModuleIdentity", "Integer32", "IpAddress", "Bits", "NotificationType", "TimeTicks", "iso", "ObjectIdentity")
DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
alvarionSatelliteManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7))
if mibBuilder.loadTexts: alvarionSatelliteManagementMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionSatelliteManagementMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionSatelliteManagementMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionSatelliteManagementMIB.setDescription('Alvarion SatelliteManagement MIB.')
alvarionSatelliteManagementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1))
satelliteInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1))
masterSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 2))
satelliteTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1), )
if mibBuilder.loadTexts: satelliteTable.setStatus('current')
if mibBuilder.loadTexts: satelliteTable.setDescription('The table of all satellite access points currently registered by the Master access point. In tabular form to allow multiple instance on an agent.')
satelliteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteIndex"))
if mibBuilder.loadTexts: satelliteEntry.setStatus('current')
if mibBuilder.loadTexts: satelliteEntry.setDescription('Information about a Satellite access point currently registered by the Master access point. satelliteIndex - Uniquely identifies a device in the satellite table.')
satelliteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: satelliteIndex.setStatus('current')
if mibBuilder.loadTexts: satelliteIndex.setDescription('Index of a the satellite in the satelliteTable.')
satelliteDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceId.setStatus('current')
if mibBuilder.loadTexts: satelliteDeviceId.setDescription('Device ID of a the satellite in the satelliteTable.')
satelliteMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMacAddress.setStatus('current')
if mibBuilder.loadTexts: satelliteMacAddress.setDescription('Indicates the MAC address of the wireless radio of the satellite access point.')
satelliteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteIpAddress.setStatus('current')
if mibBuilder.loadTexts: satelliteIpAddress.setDescription('Indicates the IP address of the satellite access point.')
satelliteName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteName.setStatus('current')
if mibBuilder.loadTexts: satelliteName.setDescription('Indicates the name of the satellite access point.')
satelliteSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 6), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSSID.setStatus('current')
if mibBuilder.loadTexts: satelliteSSID.setDescription('Indicates the SSID of the satellite access point.')
satelliteChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumber.setStatus('current')
if mibBuilder.loadTexts: satelliteChannelNumber.setDescription('Indicates the wireless channel number the satellite access point is operating on.')
satelliteForwardWirelessToWireless = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteForwardWirelessToWireless.setStatus('current')
if mibBuilder.loadTexts: satelliteForwardWirelessToWireless.setDescription("Indicates if the forwarding of traffic between wireless client stations is enabled on the satellite access point. 'true': indicates that the forwarding feature is enabled, 'false': indicates that no forwarding takes place.")
satelliteMasterTrafficOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMasterTrafficOnly.setStatus('current')
if mibBuilder.loadTexts: satelliteMasterTrafficOnly.setDescription('Indicates if the satellite will only forward traffic that is addressed to the MAC address of the Master access point.')
satelliteSNMPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSNMPPort.setStatus('current')
if mibBuilder.loadTexts: satelliteSNMPPort.setDescription('Indicates the SNMP port on which the satellite listens. The value zero is used when no information could be retrieved from the satellite device.')
satelliteSecureWebPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSecureWebPort.setStatus('current')
if mibBuilder.loadTexts: satelliteSecureWebPort.setDescription('Indicates the secure web port on which the satellite listens. The value zero is used when no information could be retrieved from the satellite device.')
satelliteDeviceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceMacAddress.setStatus('current')
if mibBuilder.loadTexts: satelliteDeviceMacAddress.setDescription('Indicates the MAC address of the satellite access point bridge interface.')
satelliteProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteProductName.setStatus('current')
if mibBuilder.loadTexts: satelliteProductName.setDescription('Indicates the Alvarion product name for the device in printable ASCII characters.')
satelliteFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: satelliteFirmwareRevision.setDescription('Indicates the revision number of the device firmware in printable ASCII characters.')
satelliteGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGroupName.setStatus('current')
if mibBuilder.loadTexts: satelliteGroupName.setDescription('Indicates the location-aware group name of the satellite. The group name is only returned when location-aware is enabled at the satellite. An empty string is returned otherwise.')
satelliteChannelNumberRadio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumberRadio2.setStatus('current')
if mibBuilder.loadTexts: satelliteChannelNumberRadio2.setDescription('Indicates the wireless channel number the radio 2 is operating on.')
satelliteVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteVLAN.setStatus('current')
if mibBuilder.loadTexts: satelliteVLAN.setDescription('Management VLAN.')
satelliteDetectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDetectionPort.setStatus('current')
if mibBuilder.loadTexts: satelliteDetectionPort.setDescription('The detection packet is send on this interface.')
satelliteNumber = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteNumber.setStatus('current')
if mibBuilder.loadTexts: satelliteNumber.setDescription('Indicates the number of satellites present in the satellite table.')
satelliteUpNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 2, 1), AlvarionNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteUpNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: satelliteUpNotificationEnabled.setDescription('Specifies if satelliteUpNotification notifications are generated.')
satelliteDownNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 1, 2, 2), AlvarionNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteDownNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: satelliteDownNotificationEnabled.setDescription('Specifies if satelliteDownNotification notifications are generated.')
alvarionSatelliteManagementMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 2))
alvarionSatelliteManagementMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 2, 0))
satelliteUpNotification = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 2, 0, 1)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteUpNotification.setStatus('current')
if mibBuilder.loadTexts: satelliteUpNotification.setDescription('Sent when a new satellite is detected.')
satelliteDownNotification = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 2, 0, 2)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteDownNotification.setStatus('current')
if mibBuilder.loadTexts: satelliteDownNotification.setDescription('Sent when a satellite becomes unreachable.')
alvarionSatelliteManagementMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3))
alvarionSatelliteManagementMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 1))
alvarionSatelliteManagementMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 2))
alvarionSatelliteManagementMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 1, 1)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "alvarionSatelliteManagementMIBGroup"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "alvarionSatelliteNotificationControlGroup"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "alvarionSatelliteNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSatelliteManagementMIBCompliance = alvarionSatelliteManagementMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionSatelliteManagementMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion SatelliteManagement MIB.')
alvarionSatelliteManagementMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 2, 1)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumber"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteForwardWirelessToWireless"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteMasterTrafficOnly"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteSNMPPort"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteSecureWebPort"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceMacAddress"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteProductName"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteFirmwareRevision"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteGroupName"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteNumber"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumberRadio2"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteVLAN"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDetectionPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSatelliteManagementMIBGroup = alvarionSatelliteManagementMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionSatelliteManagementMIBGroup.setDescription('A collection of objects providing the Satellite Management MIB capability.')
alvarionSatelliteNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 2, 2)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotificationEnabled"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSatelliteNotificationControlGroup = alvarionSatelliteNotificationControlGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionSatelliteNotificationControlGroup.setDescription('A collection of objects providing the Satellite Management MIB notification control capability.')
alvarionSatelliteNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 7, 3, 2, 3)).setObjects(("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotification"), ("ALVARION-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSatelliteNotificationGroup = alvarionSatelliteNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionSatelliteNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("ALVARION-SATELLITE-MANAGEMENT-MIB", satelliteIndex=satelliteIndex, satelliteChannelNumberRadio2=satelliteChannelNumberRadio2, satelliteInfo=satelliteInfo, masterSettings=masterSettings, satelliteSecureWebPort=satelliteSecureWebPort, satelliteMasterTrafficOnly=satelliteMasterTrafficOnly, alvarionSatelliteManagementMIBNotificationPrefix=alvarionSatelliteManagementMIBNotificationPrefix, satelliteProductName=satelliteProductName, alvarionSatelliteManagementMIB=alvarionSatelliteManagementMIB, alvarionSatelliteManagementMIBObjects=alvarionSatelliteManagementMIBObjects, satelliteNumber=satelliteNumber, satelliteDetectionPort=satelliteDetectionPort, satelliteVLAN=satelliteVLAN, satelliteFirmwareRevision=satelliteFirmwareRevision, alvarionSatelliteManagementMIBGroups=alvarionSatelliteManagementMIBGroups, satelliteDownNotificationEnabled=satelliteDownNotificationEnabled, alvarionSatelliteNotificationControlGroup=alvarionSatelliteNotificationControlGroup, satelliteDeviceMacAddress=satelliteDeviceMacAddress, satelliteChannelNumber=satelliteChannelNumber, satelliteDownNotification=satelliteDownNotification, alvarionSatelliteManagementMIBConformance=alvarionSatelliteManagementMIBConformance, satelliteUpNotificationEnabled=satelliteUpNotificationEnabled, satelliteUpNotification=satelliteUpNotification, satelliteSNMPPort=satelliteSNMPPort, satelliteName=satelliteName, satelliteForwardWirelessToWireless=satelliteForwardWirelessToWireless, satelliteTable=satelliteTable, satelliteDeviceId=satelliteDeviceId, satelliteGroupName=satelliteGroupName, satelliteMacAddress=satelliteMacAddress, alvarionSatelliteManagementMIBGroup=alvarionSatelliteManagementMIBGroup, satelliteEntry=satelliteEntry, PYSNMP_MODULE_ID=alvarionSatelliteManagementMIB, satelliteSSID=satelliteSSID, alvarionSatelliteManagementMIBCompliances=alvarionSatelliteManagementMIBCompliances, alvarionSatelliteNotificationGroup=alvarionSatelliteNotificationGroup, alvarionSatelliteManagementMIBCompliance=alvarionSatelliteManagementMIBCompliance, alvarionSatelliteManagementMIBNotifications=alvarionSatelliteManagementMIBNotifications, satelliteIpAddress=satelliteIpAddress)