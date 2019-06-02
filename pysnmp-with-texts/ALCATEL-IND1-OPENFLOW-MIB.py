#
# PySNMP MIB module ALCATEL-IND1-OPENFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-OPENFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:18:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1OpenflowMIB, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1OpenflowMIB")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, ModuleIdentity, IpAddress, Unsigned32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "ModuleIdentity", "IpAddress", "Unsigned32", "iso", "ObjectIdentity", "Bits", "Counter32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
alcatelIND1OpenflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1))
alcatelIND1OpenflowMIB.setRevisions(('2013-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1OpenflowMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1OpenflowMIB.setLastUpdated('201311080000Z')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): Openflow for OS6900 Product Line. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 2013 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1OpenflowMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 0))
alcatelIND1OpenflowMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1))
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBObjects.setDescription(' Alcatel-Lucent Openflow Managed Objects.')
alcatelIND1OpenflowMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2))
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBConformance.setDescription(' Alcatel-Lucent Openflow Conformance Information.')
alaOpenflowGlobalConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 1))
alaOpenflowGlobalBackoffMax = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOpenflowGlobalBackoffMax.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowGlobalBackoffMax.setDescription(' Alcatel-Lucent Openflow maximum back-off time in seconds for controller connection attempts.')
alaOpenflowGlobalIdleProbeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOpenflowGlobalIdleProbeTimeout.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowGlobalIdleProbeTimeout.setDescription(' Alcatel-Lucent Openflow idle probe timeout value in seconds. If set to 0, idle probing is disabled.')
alaOpenflowLogicalSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2), )
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchTable.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchTable.setDescription('This table contains one row for each Logical Switch.')
alaOpenflowLogicalSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitch"))
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchEntry.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchEntry.setDescription('Information about the Openflow Logical Switches. ')
alaOpenflowLogicalSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: alaOpenflowLogicalSwitch.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitch.setDescription('Openflow Logical Switch Name.')
alaOpenflowLogicalSwitchAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchAdminState.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchAdminState.setDescription('Logical Switch Admin State. Enable or disable the Logical Switch. When disabled, all controllers for the Logical Switch will be operationally disabled and flows added by those controllers will be removed.')
alaOpenflowLogicalSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("api", 2))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchMode.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchMode.setDescription('Openflow Logical Switch Mode. Normal is regular Openflow, API is for ACL-like flow operation. Only one Logical Switch can be in api mode at a time. This object cannot be modified after the Logical Switch has been created.')
alaOpenflowLogicalSwitchVersions = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("v1dot0", 0), ("v1dot3dot1", 1))).clone(namedValues=NamedValues(("v1dot0", 0), ("v1dot3dot1", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchVersions.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchVersions.setDescription('Openflow Logical Switch Bitmap of enabled Openflow versions. At least one version must be enabled.')
alaOpenflowLogicalSwitchVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 4093), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchVlan.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchVlan.setDescription('Openflow Logical Switch VLAN. The value 0 indicates that no VLAN has been specified, it is not a valid value to write. This object is not valid to write when creating/modifying an entry with alaOpenflowLogicalSwitchMode api(2)')
alaOpenflowLogicalSwitchControllerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchControllerCount.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchControllerCount.setDescription('Count of the configured controllers for the Logical Switch.')
alaOpenflowLogicalSwitchInterfaceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchInterfaceCount.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchInterfaceCount.setDescription('Count of the configured interfaces (ports and link aggregations) for the Logical Switch.')
alaOpenflowLogicalSwitchFlowCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchFlowCount.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchFlowCount.setDescription('Count of the flows pushed to the Logical Switch by its controllers.')
alaOpenflowLogicalSwitchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowLogicalSwitchRowStatus.setDescription('Deleting a row from this table will also remove associated entries from other tables in this mib that have a logical switch as part of their index.')
alaOpenflowControllerTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3), )
if mibBuilder.loadTexts: alaOpenflowControllerTable.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerTable.setDescription('This table contains one row for each controller on each logical switch. Currently, up to three controllers per logical switch are supported per logical switch.')
alaOpenflowControllerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerLogicalSwitch"), (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIpType"), (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIp"), (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerPort"))
if mibBuilder.loadTexts: alaOpenflowControllerEntry.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerEntry.setDescription('Information about the Openflow Controllers attached to Logical Switches. ')
alaOpenflowControllerLogicalSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: alaOpenflowControllerLogicalSwitch.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerLogicalSwitch.setDescription('Openflow Logical Switch Name.')
alaOpenflowControllerIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 2), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: alaOpenflowControllerIpType.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerIpType.setDescription('Openflow Controller IP Address Type. The only type currently supported is ipv4(1)')
alaOpenflowControllerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaOpenflowControllerIp.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerIp.setDescription('Openflow Controller IP Address. As specified by alaOpenflowControllerIpType, only ipv4 is currently supported')
alaOpenflowControllerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: alaOpenflowControllerPort.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerPort.setDescription('Openflow Controller Port.')
alaOpenflowControllerRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("equal", 1), ("master", 2), ("slave", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowControllerRole.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerRole.setDescription('Role of the Controller for the Logical Switch. The role is negotiated by the controllers and the switch is notified of the outcome (1.3.1+). 1.0 controllers will always have the role of equal. Only one controller per Logical Switch can have the role of master.')
alaOpenflowControllerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowControllerAdminState.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerAdminState.setDescription("Controller Admin State. Enable or disable connection to the controller. The Logical Switch runs in 'Fail Secure Mode' so all flow aging, etc continues unaffected when the controller is administratively disabled.")
alaOpenflowControllerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("invalid", 1), ("disabled", 2), ("sendError", 3), ("init", 4), ("connecting", 5), ("backoff", 6), ("exchangingHello", 7), ("active", 8), ("idle", 9), ("disconnected", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowControllerOperState.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerOperState.setDescription('State of the Logical Switch connection to the Controller.')
alaOpenflowControllerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowControllerRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowControllerRowStatus.setDescription('On create, if the specified logical switch does not exist in alaOpenflowLogicalSwitchTable, an entry will be created in that table. Delete does not effect alaOpenflowLogicalSwitchTable.')
alaOpenflowInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4), )
if mibBuilder.loadTexts: alaOpenflowInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterfaceTable.setDescription('This table contains one row for each interface (port or link aggregation) assigned to a logical switch. An interface can only belong to one logical switch at a time. If a logical switch in API mode exists, interfaces cannot be manually added to/deleted from it; instead, interfaces default to the API mode logical switch when not assigned to another Logical Switch. Interfaces can be reassigned from the API mode logical switch to a normal mode logical switch (by adding it to that normal mode logical switch) but not directly reassigned from one normal mode logical switch to another normal mode logical switch.')
alaOpenflowInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceLogicalSwitch"), (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterface"))
if mibBuilder.loadTexts: alaOpenflowInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterfaceEntry.setDescription('Information about the interfaces assigned to Openflow Logical Switches.')
alaOpenflowInterfaceLogicalSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: alaOpenflowInterfaceLogicalSwitch.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterfaceLogicalSwitch.setDescription('Openflow Logical Switch Name.')
alaOpenflowInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: alaOpenflowInterface.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterface.setDescription('Openflow Interface attached to a Logical Switch. Port values are dot1dBasePort values, Link Aggregations start at 32769.')
alaOpenflowInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("api", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOpenflowInterfaceMode.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterfaceMode.setDescription('Openflow Interface Mode. Normal is regular Openflow, API is for ACL like flow operation.')
alaOpenflowInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOpenflowInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowInterfaceRowStatus.setDescription('On create, if the specified logical switch does not exist in alaOpenflowLogicalSwitchTable, an entry will be created in that table. Delete does not effect alaOpenflowLogicalSwitchTable.')
alcatelIND1OpenflowMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBGroups.setDescription('Branch For ALU Openflow MIB Subsystem Units Of Conformance.')
alcatelIND1OpenflowMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1OpenflowMIBCompliances.setDescription('Branch For ALU Openflow MIB Subsystem Compliance Statements.')
alaOpenflowMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleConfigGroup"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleLogicalSwitchGroup"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleControllerGroup"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOpenflowMIBCompliance = alaOpenflowMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowMIBCompliance.setDescription('Compliance statement for Openflow.')
alaOpenflowModuleConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalBackoffMax"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalIdleProbeTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOpenflowModuleConfigGroup = alaOpenflowModuleConfigGroup.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowModuleConfigGroup.setDescription('Openflow Global Configuration Modules Group.')
alaOpenflowModuleLogicalSwitchGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchAdminState"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchMode"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVersions"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVlan"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchControllerCount"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchInterfaceCount"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchFlowCount"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOpenflowModuleLogicalSwitchGroup = alaOpenflowModuleLogicalSwitchGroup.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowModuleLogicalSwitchGroup.setDescription('Openflow Logical Switch Configuration Modules Group.')
alaOpenflowModuleControllerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRole"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerAdminState"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerOperState"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOpenflowModuleControllerGroup = alaOpenflowModuleControllerGroup.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowModuleControllerGroup.setDescription('Openflow Controller Configuration Modules Group.')
alaOpenflowModuleInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 77, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceMode"), ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOpenflowModuleInterfaceGroup = alaOpenflowModuleInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: alaOpenflowModuleInterfaceGroup.setDescription('Openflow Interface Configuration Modules Group.')
mibBuilder.exportSymbols("ALCATEL-IND1-OPENFLOW-MIB", alaOpenflowLogicalSwitchEntry=alaOpenflowLogicalSwitchEntry, alaOpenflowLogicalSwitchInterfaceCount=alaOpenflowLogicalSwitchInterfaceCount, alcatelIND1OpenflowMIBNotifications=alcatelIND1OpenflowMIBNotifications, alaOpenflowControllerRole=alaOpenflowControllerRole, alaOpenflowControllerRowStatus=alaOpenflowControllerRowStatus, alaOpenflowMIBCompliance=alaOpenflowMIBCompliance, alaOpenflowLogicalSwitchVlan=alaOpenflowLogicalSwitchVlan, alaOpenflowInterfaceMode=alaOpenflowInterfaceMode, alaOpenflowModuleLogicalSwitchGroup=alaOpenflowModuleLogicalSwitchGroup, alaOpenflowControllerPort=alaOpenflowControllerPort, alaOpenflowLogicalSwitchVersions=alaOpenflowLogicalSwitchVersions, alaOpenflowLogicalSwitchRowStatus=alaOpenflowLogicalSwitchRowStatus, alaOpenflowControllerAdminState=alaOpenflowControllerAdminState, alaOpenflowInterfaceRowStatus=alaOpenflowInterfaceRowStatus, alcatelIND1OpenflowMIBCompliances=alcatelIND1OpenflowMIBCompliances, alaOpenflowLogicalSwitchAdminState=alaOpenflowLogicalSwitchAdminState, alaOpenflowLogicalSwitchFlowCount=alaOpenflowLogicalSwitchFlowCount, PYSNMP_MODULE_ID=alcatelIND1OpenflowMIB, alaOpenflowInterfaceTable=alaOpenflowInterfaceTable, alaOpenflowControllerOperState=alaOpenflowControllerOperState, alaOpenflowModuleInterfaceGroup=alaOpenflowModuleInterfaceGroup, alcatelIND1OpenflowMIBObjects=alcatelIND1OpenflowMIBObjects, alcatelIND1OpenflowMIBGroups=alcatelIND1OpenflowMIBGroups, alaOpenflowControllerLogicalSwitch=alaOpenflowControllerLogicalSwitch, alcatelIND1OpenflowMIB=alcatelIND1OpenflowMIB, alaOpenflowLogicalSwitch=alaOpenflowLogicalSwitch, alaOpenflowControllerIp=alaOpenflowControllerIp, alcatelIND1OpenflowMIBConformance=alcatelIND1OpenflowMIBConformance, alaOpenflowControllerTable=alaOpenflowControllerTable, alaOpenflowControllerIpType=alaOpenflowControllerIpType, alaOpenflowInterfaceEntry=alaOpenflowInterfaceEntry, alaOpenflowLogicalSwitchMode=alaOpenflowLogicalSwitchMode, alaOpenflowInterfaceLogicalSwitch=alaOpenflowInterfaceLogicalSwitch, alaOpenflowModuleControllerGroup=alaOpenflowModuleControllerGroup, alaOpenflowControllerEntry=alaOpenflowControllerEntry, alaOpenflowInterface=alaOpenflowInterface, alaOpenflowGlobalIdleProbeTimeout=alaOpenflowGlobalIdleProbeTimeout, alaOpenflowLogicalSwitchControllerCount=alaOpenflowLogicalSwitchControllerCount, alaOpenflowLogicalSwitchTable=alaOpenflowLogicalSwitchTable, alaOpenflowGlobalConfigObjects=alaOpenflowGlobalConfigObjects, alaOpenflowModuleConfigGroup=alaOpenflowModuleConfigGroup, alaOpenflowGlobalBackoffMax=alaOpenflowGlobalBackoffMax)