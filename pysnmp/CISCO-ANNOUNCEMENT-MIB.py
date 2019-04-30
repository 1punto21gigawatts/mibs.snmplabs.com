#
# PySNMP MIB module CISCO-ANNOUNCEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ANNOUNCEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
cmgwIndex, = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Unsigned32, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, Bits, NotificationType, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "Bits", "NotificationType", "TimeTicks", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoAnnouncementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 8888))
ciscoAnnouncementMIB.setRevisions(('2003-03-25 00:00',))
if mibBuilder.loadTexts: ciscoAnnouncementMIB.setLastUpdated('200303250000Z')
if mibBuilder.loadTexts: ciscoAnnouncementMIB.setOrganization('Cisco Systems, Inc.')
ciscoAnnouncementMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 0))
ciscoAnnouncementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1))
ciscoAnnouncementMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2))
cannoGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1))
cannoControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1))
cannoAudioFileConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2))
cannoControlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1), )
if mibBuilder.loadTexts: cannoControlTable.setStatus('current')
cannoControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"))
if mibBuilder.loadTexts: cannoControlEntry.setStatus('current')
cannoAudioFileServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoAudioFileServerName.setStatus('current')
cannoDnResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internalOnly", 1), ("externalOnly", 2))).clone('internalOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoDnResolution.setStatus('current')
cannoIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoIpAddressType.setStatus('current')
cannoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 4), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoIpAddress.setStatus('current')
cannoAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(10080)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoAgeTime.setStatus('current')
cannoSubDirPath = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoSubDirPath.setStatus('current')
cannoReqTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 50)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoReqTimeout.setStatus('current')
cannoMaxPermanent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500)).clone(41)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cannoMaxPermanent.setStatus('current')
cannoAudioFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1), )
if mibBuilder.loadTexts: cannoAudioFileTable.setStatus('current')
cannoAudioFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"), (0, "CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileNumber"))
if mibBuilder.loadTexts: cannoAudioFileEntry.setStatus('current')
cannoAudioFileNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999)))
if mibBuilder.loadTexts: cannoAudioFileNumber.setStatus('current')
cannoAudioFileDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileDescr.setStatus('current')
cannoAudioFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileName.setStatus('current')
cannoAudioFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cached", 1), ("loading", 2), ("invalidFile", 3), ("loadFailed", 4), ("notCached", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cannoAudioFileStatus.setStatus('current')
cannoAudioFileOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inPlaying", 1), ("notPlaying", 2), ("delPending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cannoAudioFileOperStatus.setStatus('current')
cannoAudioFilePlayNoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFilePlayNoc.setStatus('current')
cannoAudioFileDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('10 milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileDuration.setStatus('current')
cannoAudioFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("permanent", 2))).clone('dynamic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileType.setStatus('current')
cannoAudioFileAge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cannoAudioFileAge.setStatus('current')
cannoAudioFileAdminDeletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gracefully", 1), ("forcefully", 2))).clone('gracefully')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileAdminDeletion.setStatus('current')
cannoAudioFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 8888, 1, 1, 2, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cannoAudioFileRowStatus.setStatus('current')
cannoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 1))
cannoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2))
cannoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 1, 1)).setObjects(("CISCO-ANNOUNCEMENT-MIB", "cannoControlGroup"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cannoMIBCompliance = cannoMIBCompliance.setStatus('current')
cannoControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2, 1)).setObjects(("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileServerName"), ("CISCO-ANNOUNCEMENT-MIB", "cannoDnResolution"), ("CISCO-ANNOUNCEMENT-MIB", "cannoIpAddressType"), ("CISCO-ANNOUNCEMENT-MIB", "cannoIpAddress"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAgeTime"), ("CISCO-ANNOUNCEMENT-MIB", "cannoSubDirPath"), ("CISCO-ANNOUNCEMENT-MIB", "cannoReqTimeout"), ("CISCO-ANNOUNCEMENT-MIB", "cannoMaxPermanent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cannoControlGroup = cannoControlGroup.setStatus('current')
cannoAudioFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 8888, 2, 2, 2)).setObjects(("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileDescr"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileName"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileStatus"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileOperStatus"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFilePlayNoc"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileDuration"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileType"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileAge"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileAdminDeletion"), ("CISCO-ANNOUNCEMENT-MIB", "cannoAudioFileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cannoAudioFileGroup = cannoAudioFileGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ANNOUNCEMENT-MIB", cannoAudioFileConfig=cannoAudioFileConfig, cannoAudioFileServerName=cannoAudioFileServerName, cannoAudioFileName=cannoAudioFileName, cannoMaxPermanent=cannoMaxPermanent, cannoIpAddress=cannoIpAddress, PYSNMP_MODULE_ID=ciscoAnnouncementMIB, ciscoAnnouncementMIBConformance=ciscoAnnouncementMIBConformance, cannoAudioFileOperStatus=cannoAudioFileOperStatus, cannoSubDirPath=cannoSubDirPath, cannoAudioFileStatus=cannoAudioFileStatus, cannoMIBCompliances=cannoMIBCompliances, cannoAudioFileGroup=cannoAudioFileGroup, cannoMIBGroups=cannoMIBGroups, cannoDnResolution=cannoDnResolution, cannoAudioFileType=cannoAudioFileType, cannoAudioFileDescr=cannoAudioFileDescr, cannoAudioFileTable=cannoAudioFileTable, ciscoAnnouncementMIBNotifs=ciscoAnnouncementMIBNotifs, cannoGeneric=cannoGeneric, cannoReqTimeout=cannoReqTimeout, cannoAudioFileDuration=cannoAudioFileDuration, cannoAudioFilePlayNoc=cannoAudioFilePlayNoc, cannoAudioFileNumber=cannoAudioFileNumber, cannoControlConfig=cannoControlConfig, cannoAudioFileRowStatus=cannoAudioFileRowStatus, cannoIpAddressType=cannoIpAddressType, cannoControlEntry=cannoControlEntry, cannoAgeTime=cannoAgeTime, cannoControlGroup=cannoControlGroup, cannoAudioFileEntry=cannoAudioFileEntry, cannoAudioFileAdminDeletion=cannoAudioFileAdminDeletion, cannoControlTable=cannoControlTable, ciscoAnnouncementMIB=ciscoAnnouncementMIB, cannoAudioFileAge=cannoAudioFileAge, ciscoAnnouncementMIBObjects=ciscoAnnouncementMIBObjects, cannoMIBCompliance=cannoMIBCompliance)