#
# PySNMP MIB module CISCO-ENTITY-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-PROVISIONING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, ModuleIdentity, NotificationType, iso, Gauge32, Unsigned32, TimeTicks, Integer32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "NotificationType", "iso", "Gauge32", "Unsigned32", "TimeTicks", "Integer32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Bits")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
ciscoEntityProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 139))
if mibBuilder.loadTexts: ciscoEntityProvMIB.setLastUpdated('9907082052Z')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-dslam@cisco.com')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setDescription("This MIB module defines the objects that support provisioning of 'container' class physical entities. Provisioning sets up a 'container' to hold a specified physical entity. This allows a management client to configure the specified physical entity, including all of its subordinates physical entities, before installation. Consider a network manager of a CLEC (Competitive Local Exchange Carrier) planning for the installation of the hardware necessary to support several new subscribers. This network manager wants to pre-configure the ADSL (Asymmetric Digital Subscriber Loop) modems that will support these subscribers, thereby reducing the bring-up time once they arrive. Under normal circumstances this would not be possible. However, provisioning allows the network manager to 'create' the physical entities that represent the new modems. In essence, the device simulates the installation of the new modules into the system. This has the effect of creating all conceptual rows in all the necessary tables that support the physical entity and all its subordinate physical entities (e.g., entPhysicalTable, entAliasMappingTable, and ifTable).")
ciscoEntityProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 1))
ceProvContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1), )
if mibBuilder.loadTexts: ceProvContainerTable.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerTable.setDescription("This table extends some entries in the entPhysicalTable (see ENTITY-MIB for further details). A entry appears in this table for a physical entity matching the following criteria: 1) Its entPhysicalClass object has a value of 'container'; 2) It can contain one (but not multiple) physical entity; and, 3) It supports provisioning.")
ceProvContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceProvContainerEntry.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerEntry.setDescription("The attributes that support the provisioning of a physical entity of the 'container' class (i.e., a physical entity having an entPhysicalClass of 'container').")
ceProvContainerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequipped", 1), ("provisioned", 2), ("mismatched", 3), ("invalid", 4), ("equipped", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerStatus.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerStatus.setDescription("This object represents the equipment status of the container: 'unequipped' The container neither holds a physical entity, nor has it been provisioned to hold a physical entity. 'provisioned' The container does not hold a physical entity However, it has been provisioned to hold a physical entity of a particular type. This physical entity appears in the entPhysicalTable as a child of the container. 'mismatched' The container holds a valid physical entity that does not match the type of physical entity for which the container has been previously provisioned. 'invalid' The container holds a recognized physical entity that the container is not capable of supporting, or the container holds an unrecognized physical entity. 'equipped' The container holds a valid physical entity for which the container has been previously provisioned to hold. 'failed' The container holds a valid physical entity that has become totally inoperable and incapable of providing service.")
ceProvContainerEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceProvContainerEquipped.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerEquipped.setDescription("This object specifies the vendor type of the physical entity for which this container has been provisioned to hold. If the container has no provisioning, then the value of this object is { 0 0 }. For more information concerning 'vendor type', see the definition of the entPhysicalVendorType object in the ENTITY-MIB.")
ceProvContainerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerDetected.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerDetected.setDescription("This object specifies the vendor type of the physical entity held by the container. If the container does not hold a physical entity, then the value of this object is { 0 0 }. For more information concerning 'vendor type', see the definition of the entPhysicalVendorType object in the ENTITY-MIB.")
ceProvMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2))
ceProvMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0))
ceProvMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3))
ceProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1))
ceProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2))
ceProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvMIBCompliance = ceProvMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ceProvMIBCompliance.setDescription('The compliance statement for entities that implement the CISCO-ENTITY-PROVISIONING-MIB. Implementation of this MIB is strongly recommended for any platform targeted for a carrier-class environment.')
ceProvContainerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvContainerGroup = ceProvContainerGroup.setStatus('current')
if mibBuilder.loadTexts: ceProvContainerGroup.setDescription("A collection of attributes that support provisioning of a physical entity of the 'container' class.")
mibBuilder.exportSymbols("CISCO-ENTITY-PROVISIONING-MIB", ceProvContainerEquipped=ceProvContainerEquipped, ceProvContainerDetected=ceProvContainerDetected, ceProvContainerStatus=ceProvContainerStatus, ceProvContainerTable=ceProvContainerTable, ceProvContainerEntry=ceProvContainerEntry, ciscoEntityProvMIB=ciscoEntityProvMIB, ciscoEntityProvMIBObjects=ciscoEntityProvMIBObjects, ceProvMIBGroups=ceProvMIBGroups, ceProvMIBNotificationsPrefix=ceProvMIBNotificationsPrefix, ceProvMIBCompliances=ceProvMIBCompliances, ceProvContainerGroup=ceProvContainerGroup, ceProvMIBNotifications=ceProvMIBNotifications, PYSNMP_MODULE_ID=ciscoEntityProvMIB, ceProvMIBCompliance=ceProvMIBCompliance, ceProvMIBConformance=ceProvMIBConformance)