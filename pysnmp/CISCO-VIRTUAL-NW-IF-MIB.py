#
# PySNMP MIB module CISCO-VIRTUAL-NW-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIRTUAL-NW-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcAddressId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcAddressId")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifName, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, TimeTicks, Counter64, iso, NotificationType, Integer32, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "iso", "NotificationType", "Integer32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoVirtualNwIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 290))
ciscoVirtualNwIfMIB.setRevisions(('2002-10-02 00:00',))
if mibBuilder.loadTexts: ciscoVirtualNwIfMIB.setLastUpdated('200210020000Z')
if mibBuilder.loadTexts: ciscoVirtualNwIfMIB.setOrganization('Cisco Systems Inc.')
ciscoVirtualNwIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 1))
virtualNwIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 2))
virtualNwIfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1))
virtualNwIfStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 2))
virtualNwIfNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3))
virtualNwIfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0))
virtualNwIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1), )
if mibBuilder.loadTexts: virtualNwIfTable.setStatus('current')
virtualNwIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfType"), (0, "CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfId"))
if mibBuilder.loadTexts: virtualNwIfEntry.setStatus('current')
virtualNwIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vsan", 1), ("vlan", 2))))
if mibBuilder.loadTexts: virtualNwIfType.setStatus('current')
virtualNwIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: virtualNwIfId.setStatus('current')
virtualNwIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualNwIfIndex.setStatus('current')
virtualNwIfFcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 4), FcAddressId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualNwIfFcId.setStatus('current')
virtualNwIfOperStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("adminDown", 2), ("vsanNotOperational", 3), ("noFcid", 4), ("kernelConfFailure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualNwIfOperStatusCause.setStatus('current')
virtualNwIfOperStatusCauseDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualNwIfOperStatusCauseDescr.setStatus('current')
virtualNwIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualNwIfRowStatus.setStatus('current')
virtualNwIfCreateEntryNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0, 1)).setObjects(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: virtualNwIfCreateEntryNotify.setStatus('current')
virtualNwIfDeleteEntryNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 290, 1, 3, 0, 2)).setObjects(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex"))
if mibBuilder.loadTexts: virtualNwIfDeleteEntryNotify.setStatus('current')
virtualNwIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 1))
virtualNwIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2))
virtualNwIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 1, 1)).setObjects(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfGroup"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualNwIfMIBCompliance = virtualNwIfMIBCompliance.setStatus('current')
virtualNwIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2, 1)).setObjects(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfIndex"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfFcId"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfOperStatusCause"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfOperStatusCauseDescr"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualNwIfGroup = virtualNwIfGroup.setStatus('current')
virtualNwIfNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 290, 2, 2, 2)).setObjects(("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfCreateEntryNotify"), ("CISCO-VIRTUAL-NW-IF-MIB", "virtualNwIfDeleteEntryNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualNwIfNotificationGroup = virtualNwIfNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIRTUAL-NW-IF-MIB", virtualNwIfNotificationGroup=virtualNwIfNotificationGroup, virtualNwIfIndex=virtualNwIfIndex, virtualNwIfCreateEntryNotify=virtualNwIfCreateEntryNotify, PYSNMP_MODULE_ID=ciscoVirtualNwIfMIB, virtualNwIfMIBCompliances=virtualNwIfMIBCompliances, virtualNwIfMIBConformance=virtualNwIfMIBConformance, virtualNwIfNotification=virtualNwIfNotification, virtualNwIfMIBCompliance=virtualNwIfMIBCompliance, virtualNwIfStatistics=virtualNwIfStatistics, virtualNwIfFcId=virtualNwIfFcId, virtualNwIfGroup=virtualNwIfGroup, virtualNwIfTable=virtualNwIfTable, virtualNwIfId=virtualNwIfId, virtualNwIfRowStatus=virtualNwIfRowStatus, virtualNwIfMIBGroups=virtualNwIfMIBGroups, ciscoVirtualNwIfMIB=ciscoVirtualNwIfMIB, ciscoVirtualNwIfObjects=ciscoVirtualNwIfObjects, virtualNwIfOperStatusCause=virtualNwIfOperStatusCause, virtualNwIfConfig=virtualNwIfConfig, virtualNwIfDeleteEntryNotify=virtualNwIfDeleteEntryNotify, virtualNwIfOperStatusCauseDescr=virtualNwIfOperStatusCauseDescr, virtualNwIfNotifications=virtualNwIfNotifications, virtualNwIfEntry=virtualNwIfEntry, virtualNwIfType=virtualNwIfType)