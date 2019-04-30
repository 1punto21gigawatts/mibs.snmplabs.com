#
# PySNMP MIB module ASCEND-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-SESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
sessionStatusGroup, = mibBuilder.importSymbols("ASCEND-MIB", "sessionStatusGroup")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ObjectIdentity, TimeTicks, iso, ModuleIdentity, MibIdentifier, NotificationType, Integer32, IpAddress, Counter64, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ObjectIdentity", "TimeTicks", "iso", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "IpAddress", "Counter64", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

ssnStatusMaximumSessions = MibScalar((1, 3, 6, 1, 4, 1, 529, 12, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusMaximumSessions.setStatus('mandatory')
sessionStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 2), )
if mibBuilder.loadTexts: sessionStatusTable.setStatus('mandatory')
sessionStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 2, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "ssnStatusIndex"))
if mibBuilder.loadTexts: sessionStatusEntry.setStatus('mandatory')
ssnStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusIndex.setStatus('mandatory')
ssnStatusValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssnStatusValidFlag.setStatus('mandatory')
ssnStatusUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserName.setStatus('mandatory')
ssnStatusUserIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserIPAddress.setStatus('mandatory')
ssnStatusUserSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserSubnetMask.setStatus('mandatory')
ssnStatusCurrentService = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("ppp", 3), ("slip", 4), ("mpp", 5), ("x25", 6), ("combinet", 7), ("frameRelay", 8), ("euraw", 9), ("euui", 10), ("telnet", 11), ("telnetBinary", 12), ("rawTcp", 13), ("terminalServer", 14), ("mp", 15), ("virtualConnect", 16), ("dchannelX25", 17), ("dtpt", 18), ("ipFax", 19), ("atm", 20), ("hdlcNrm", 21), ("voip", 22), ("visa2", 23), ("netToNet", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusCurrentService.setStatus('mandatory')
ssnStatusCallReferenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusCallReferenceNum.setStatus('mandatory')
sessionActiveTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 3), )
if mibBuilder.loadTexts: sessionActiveTable.setStatus('mandatory')
sessionActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 3, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "ssnActiveCallReferenceNum"))
if mibBuilder.loadTexts: sessionActiveEntry.setStatus('mandatory')
ssnActiveCallReferenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveCallReferenceNum.setStatus('mandatory')
ssnActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveIndex.setStatus('mandatory')
ssnActiveValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssnActiveValidFlag.setStatus('mandatory')
ssnActiveUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserName.setStatus('mandatory')
ssnActiveUserIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserIPAddress.setStatus('mandatory')
ssnActiveUserSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserSubnetMask.setStatus('mandatory')
ssnActiveCurrentService = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("ppp", 3), ("slip", 4), ("mpp", 5), ("x25", 6), ("combinet", 7), ("frameRelay", 8), ("euraw", 9), ("euui", 10), ("telnet", 11), ("telnetBinary", 12), ("rawTcp", 13), ("terminalServer", 14), ("mp", 15), ("virtualConnect", 16), ("dchannelX25", 17), ("dtpt", 18), ("ipFax", 19), ("atm", 20), ("hdlcNrm", 21), ("voip", 22), ("visa2", 23), ("netToNet", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveCurrentService.setStatus('mandatory')
ssnActiveIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveIdleTime.setStatus('mandatory')
mppActiveStatsTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 4), )
if mibBuilder.loadTexts: mppActiveStatsTable.setStatus('mandatory')
mppActiveStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 4, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "mppStatsMpID"))
if mibBuilder.loadTexts: mppActiveStatsEntry.setStatus('mandatory')
mppStatsMpID = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsMpID.setStatus('mandatory')
mppStatsRemoteName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsRemoteName.setStatus('mandatory')
mppStatsQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("good", 1), ("fair", 2), ("marginal", 3), ("poor", 4), ("na", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsQuality.setStatus('mandatory')
mppStatsBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsBandwidth.setStatus('mandatory')
mppStatsTotalChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsTotalChannels.setStatus('mandatory')
mppStatsCLU = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsCLU.setStatus('mandatory')
mppStatsALU = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsALU.setStatus('mandatory')
mppStatsStartingTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsStartingTimeStamp.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-SESSION-MIB", sessionActiveTable=sessionActiveTable, mppStatsALU=mppStatsALU, ssnStatusUserIPAddress=ssnStatusUserIPAddress, mppStatsRemoteName=mppStatsRemoteName, sessionStatusTable=sessionStatusTable, DisplayString=DisplayString, mppStatsMpID=mppStatsMpID, ssnActiveValidFlag=ssnActiveValidFlag, mppStatsQuality=mppStatsQuality, ssnStatusMaximumSessions=ssnStatusMaximumSessions, ssnActiveUserIPAddress=ssnActiveUserIPAddress, mppStatsStartingTimeStamp=mppStatsStartingTimeStamp, ssnActiveUserSubnetMask=ssnActiveUserSubnetMask, sessionActiveEntry=sessionActiveEntry, ssnStatusCurrentService=ssnStatusCurrentService, mppStatsBandwidth=mppStatsBandwidth, ssnActiveCurrentService=ssnActiveCurrentService, ssnActiveUserName=ssnActiveUserName, ssnStatusCallReferenceNum=ssnStatusCallReferenceNum, ssnActiveIdleTime=ssnActiveIdleTime, ssnStatusUserSubnetMask=ssnStatusUserSubnetMask, ssnStatusIndex=ssnStatusIndex, mppStatsTotalChannels=mppStatsTotalChannels, mppActiveStatsTable=mppActiveStatsTable, ssnStatusValidFlag=ssnStatusValidFlag, ssnActiveIndex=ssnActiveIndex, sessionStatusEntry=sessionStatusEntry, mppActiveStatsEntry=mppActiveStatsEntry, mppStatsCLU=mppStatsCLU, ssnActiveCallReferenceNum=ssnActiveCallReferenceNum, ssnStatusUserName=ssnStatusUserName)