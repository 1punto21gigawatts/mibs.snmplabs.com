#
# PySNMP MIB module BN-LOG-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BN-LOG-MESSAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
bnLogMsg, = mibBuilder.importSymbols("S5-ROOT-MIB", "bnLogMsg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, TimeTicks, iso, Bits, Unsigned32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "iso", "Bits", "Unsigned32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibIdentifier")
TruthValue, DisplayString, TextualConvention, DateAndTime, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "DateAndTime", "RowStatus")
bnLogMsgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1))
bnLogMsgMIB.setRevisions(('2013-10-10 00:00', '2012-04-10 00:00', '2012-03-26 00:00', '2011-04-20 00:00', '2010-06-29 00:00', '2009-04-15 00:00', '2009-04-14 00:00', '2009-03-31 00:00', '2009-03-23 00:00', '2007-09-04 00:00', '2005-05-04 00:00', '2005-04-27 00:00', '2003-02-24 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bnLogMsgMIB.setRevisionsDescriptions(('v14: Corrected the syntax of bnLogMsgClearMessageBuffers.', 'v13: Changed connectionTypeNone to connectionTypeTCPSecure for bnLogMsgRemoteSyslogPrimaryConnectionType, bnLogMsgRemoteSyslogSecondaryConnectionType.', 'v12: Added bnLogMsgRemoteSyslogPrimaryTcpPort, bnLogMsgRemoteSyslogSecondaryTcpPort, bnLogMsgRemoteSyslogPrimaryConnectionType, bnLogMsgRemoteSyslogSecondaryConnectionType.', 'v11: Added bnLogMsgRemoteServerStandardSaveTargets.', 'v10: Added bnLogMsgBufferMsgType.', 'v9: Added fltNone.', 'v8: Added bnLogMsgRemoteSyslogFacility.', 'v7: Added bnLogMsgRemoteServerTable.', 'v6: Added bnLogMsgRemoteSyslogSecondaryInetAddressType and bnLogMsgRemoteSyslogSecondaryInetAddress.', 'v5: Added IPv6 support.', 'v4: Added ranges to INDEX objects.', 'v3: Added msgBufferSizeVeryLarge to bnLogMsgBufferMaxSize', 'v002: Updated by David Levi: - formatting cleanup - removed conformance/compliance sections, not needed for a proprietary MIB - added enumerations to bnLogMsgSaveTargets to reverse selection of log levels to save - added bnLogMsgRemoteSyslogEnabled - added bnLogMsgRemoteSyslogAddress - added bnLogMsgRemoteSyslogSaveTargets - added bnLogMsgClearMessageBuffers - added bnLogMsgBufferMsgUtcTime to bnLogMsgBufferTable',))
if mibBuilder.loadTexts: bnLogMsgMIB.setLastUpdated('201310100000Z')
if mibBuilder.loadTexts: bnLogMsgMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: bnLogMsgMIB.setContactInfo('Global Optical Customer Service Tel: 1-800 (ASK-TRAN) or 1-800 (ASK-ETAS)')
if mibBuilder.loadTexts: bnLogMsgMIB.setDescription('The management information definitions for the Bay Networks log message facility.')
bnLogMsgMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1))
bnLogMsgMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2))
bnLogMsgMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 3))
bnLogMsgBufferOperaton = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferOperaton.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferOperaton.setDescription('The decision to store or discard generated log messages is determined by the value of this object. Specifying on(1) causes log messages to be stored in the log message buffer facility according to the parameters specified by related management objects in this module. Specifying off(2) discontinues log message accumulation. Previously collected log messages remained stored in the buffer facility until they are manually cleared or the system is reset. Resets do not clear log messages that have been saved in non-volatile storage. Note that this object does not affect operation of the remote syslog facility, it only determines whether log messages are stored locally.')
bnLogMsgBufferMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 100, 200, 400))).clone(namedValues=NamedValues(("msgBufferSizeSmall", 50), ("msgBufferSizeMedium", 100), ("msgBufferSizeLarge", 200), ("msgBufferSizeVeryLarge", 400))).clone('msgBufferSizeSmall')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferMaxSize.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMaxSize.setDescription('This object determines the overall size of the log message buffer facilities. Changing the value of this object causes all messages currently being stored in the buffer to be lost. Note that attempts to set this object to a larger value (e.g., msgBufferSizeSmall(50) to msgBufferSizeLarge(200)) may be rejected due to current resource utiliztion within the running system. Note that this object only applies to the buffering capabilities that are volatile. Messages that are classified as volatile are lost upon system reinitialization. This object has no affect on non-volatile message logging capacity.')
bnLogMsgBufferCurSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferCurSize.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferCurSize.setDescription('The current number of log messages in the volatile portion of the system log message facility. Messages that are classified as volatile are lost upon system reinitialization.')
bnLogMsgBufferFullAction = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("overwrite", 1), ("latch", 2))).clone('overwrite')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferFullAction.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferFullAction.setDescription('The amount of buffer space allocated for log messages, as determined by the object bnLogMsgBufferMaxSize, is finite and thus only a limited amount of log messages may be saved on the device. This object specifies the action to take when this space is exhausted. Selecting overwrite(1) will cause previous messages to be over- written. Messages are overwritten based on FIFO. Specifying latch(2) causes no more messages to be saved until this object is changed to overwrite(1) or until the buffer space is made available through some other means (e.g., clearing the buffer). Note that this object only pertains to messages that are maintained in volatile storage. Messages that are saved in non-volatile storage are never overwritten. They must be cleared manually using the object bnLogMsgBufferClearTargets.')
bnLogMsgBufferSaveTargets = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeNone", 4))).clone('msgTypeCritical')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferSaveTargets.setDescription("This object determines the type of log messages that will be saved in the log message buffer facilities. Messages are classified based on their type Selecting a type of msgTypeCritical(1), msgTypeSerious(2), or msgTypeInformational(3), causes all log messages that have an associated value less than or equal to the type value specified to be saved when the log message is entered into the system. For example, specifying the value msgTypeCritical(1) causes only messages classified as 'critical' to be saved to non-volatile storage. Specifying msgTypeSerious(2) causes 'critical' and 'serious' messages to be saved. Specifying a value of msgTypeNone(4) means no log messages will be stored in volatile memory.")
bnLogMsgBufferClearTargets = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeAllVolatile", 4), ("msgTypeNonVolatile", 5))).clone('msgTypeAllVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferClearTargets.setStatus('deprecated')
if mibBuilder.loadTexts: bnLogMsgBufferClearTargets.setDescription('This object determines the type of log messages that will be deleted from the log message buffer facilities when the action object bnLogMsgBufferClearMsgs is set. Messages are classified based on their type. Specifying msgTypeAllVolatile(4) causes all messages in volatile storage to be deleted. Specifying msgTypeNonVolatile(5) causes all messages, including those in non-volatile storage, to be discarded.')
bnLogMsgBufferClearMsgs = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearMsgs", 1), ("savingMsgs", 2))).clone('savingMsgs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferClearMsgs.setStatus('deprecated')
if mibBuilder.loadTexts: bnLogMsgBufferClearMsgs.setDescription('Setting this object to clearMsgs(1) causes messages currently saved in the log message buffer facilities to be deleted. The type of entries to be deleted is determined by the bnLogMsgBufferClearTargets object. This object always returns the value savingMsgs(2) upon retrieval.')
bnLogMsgBufferNonVolCurSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferNonVolCurSize.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferNonVolCurSize.setDescription('The current number of log messages that are present in the non-volatile portion of the system log message facility. Messages that are classified as non- volatile are saved across system reinitializations.')
bnLogMsgBufferNonVolSaveTargets = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeNone", 4))).clone('msgTypeNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgBufferNonVolSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferNonVolSaveTargets.setDescription("This object determines the type of log messages that will be saved to non-volatile storage when they occur. Messages are classified based on their type. Selecting a type value causes all log messages that have an associated value less than or equal to the type value specified to be saved when the log message is entered into the system. For example, specifying the value msgTypeCritical(1) causes only messages classified as 'critical' to be saved to non-volatile storage. Specifying msgTypeSerious(2) causes 'critical' and 'serious' messages to be saved. Specifying msgTypeNone(4) causes no messages to be saved. Note that non-volatile storage space is quite limited in many systems such that the user should exercise caution when specifying the type of log messages that are to be saved in non-volatile storage. Messages are no longer saved in non-volatile storage when this space is exhausted. A log message is automatically generated to alert the user of this situation.")
bnLogMsgBufferTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10), )
if mibBuilder.loadTexts: bnLogMsgBufferTable.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferTable.setDescription('Locally held information about log messages.')
bnLogMsgBufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1), ).setIndexNames((0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgOrig"), (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgTime"), (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgBufferMsgIndex"))
if mibBuilder.loadTexts: bnLogMsgBufferEntry.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferEntry.setDescription('Information on a particular event as described by a log message and related information.')
bnLogMsgBufferMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: bnLogMsgBufferMsgIndex.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgIndex.setDescription('The arbitrary integer index assigned to the log message upon entry into the message facility.')
bnLogMsgBufferMsgOrig = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: bnLogMsgBufferMsgOrig.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgOrig.setDescription('The originator of the log message. Typically, this value represents the slot or unit on which this message originated.')
bnLogMsgBufferMsgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 3), TimeTicks())
if mibBuilder.loadTexts: bnLogMsgBufferMsgTime.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgTime.setDescription('The time (in hundredths of a second) between system initialization and the time this log message was entered into the system. This object is the second component in an index into this table to support retrieving messages ordered by time of occurrence.')
bnLogMsgBufferMsgSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("msgSrcRunning", 1), ("msgSrcNonVol", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgSrc.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgSrc.setDescription('The message source indicates whether this message was loaded from non-volatile storage at system initialization or whether the message has been generated since this time.')
bnLogMsgBufferMsgCode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgCode.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgCode.setDescription('The message code indicating the originator of and the reason why a log message has been generated. This code, coupled with the log message parameters that are associated with the message, should provide a thorough understanding of the log message.')
bnLogMsgBufferMsgString = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgString.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgString.setDescription('A printable string indicating the originator of and the reason why a log message has been generated. This string, coupled with the log message parameters that are associated with the message, should provide a thorough understanding of the log message.')
bnLogMsgBufferMsgParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam1.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam1.setDescription('A parameter that is used to convey additional information about a particular occurrence that has initiated the generation of a log message. The value of this is object is pertinent only under the context of additional information in the log entry (i.e., bnLogMsgBufferMsgCode).')
bnLogMsgBufferMsgParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam2.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam2.setDescription('A parameter that is used to convey additional information about a particular occurrence that has initiated the generation of a log message. The value of this is object is pertinent only under the context of additional information in the log entry (i.e., bnLogMsgBufferMsgCode).')
bnLogMsgBufferMsgParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam3.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgParam3.setDescription('A parameter that is used to convey additional information about a particular occurrence that has initiated the generation of a log message. The value of this is object is pertinent only under the context of additional information in the log entry (i.e., bnLogMsgBufferMsgCode).')
bnLogMsgBufferMsgUtcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgUtcTime.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgUtcTime.setDescription("Contains the system's local value of UTC (Universal Coordinated Time) when the log entry was created.")
bnLogMsgBufferMsgType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 10, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeNone", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnLogMsgBufferMsgType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferMsgType.setDescription("The message type indicates whether this message is classified as 'critical', 'serious' or 'informational'.")
bnLogMsgRemoteSyslogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogEnabled.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogEnabled.setDescription('This object controls whether remote logging of log messages using the remote syslog facility is enabled. The value of this object may not be true(2) if the value of the remote syslog address object is 0.0.0.0.')
bnLogMsgRemoteSyslogAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 12), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogAddress.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogAddress.setDescription('The IP address to which log messages are sent using the remote syslog facility. If the value of this object is 0.0.0.0, the refer to the values of bnLogMsgRemoteSyslogInetAddressType and bnLogMsgRemoteSyslogInetAddress.')
bnLogMsgRemoteSyslogSaveTargets = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeNone", 4))).clone('msgTypeCritical')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSaveTargets.setDescription("This object determines the type of log messages that will be sent to a remote syslog server when they occur. Messages are classified based on their type. Selecting a type value causes all log messages that have an associated value less than or equal to the type value specified to be sent when the log message is entered into the system. For example, specifying the value msgTypeCritical(1) causes only messages classified as 'critical' to be sent to the remote syslog server. Specifying msgTypeSerious(2) causes 'critical' and 'serious' messages to be sent. Specifying msgTypeNone(4) means that no log messages will be sent to the remote syslog server.")
bnLogMsgClearMessageBuffers = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 14), Bits().clone(namedValues=NamedValues(("none", 0), ("volCritical", 1), ("volSerious", 2), ("volInformational", 3), ("nonVolCritical", 4), ("nonVolSerious", 5), ("nonVolInformational", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgClearMessageBuffers.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgClearMessageBuffers.setDescription("Setting this objects causes messages currently saved in the log message buffer facilities to be deleted. All messages of types matching the specified bits will be deleted. For example, a Set on this object containing bits volSerious(2) and nonVolCritical(4) will delete all 'serious' messages from volatile storage, and all 'critical' messages from non-volatile storage. The none(0) value doesn't have any effect at read and write operations. It have been introduced to correct the BITS syntax declaration.")
bnLogMsgRemoteSyslogInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 15), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogInetAddressType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogInetAddressType.setDescription('The type of the IP address contained in the object bnLogMsgRemoteSyslogInetAddress. Together, these two objects specify the IP address to which log messages are sent using the remote syslog facility. The value of this object may not be unknown(0) if the value of bnLogMsgRemoteSyslogEnabled is true(2).')
bnLogMsgRemoteSyslogInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 16), InetAddress().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogInetAddress.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogInetAddress.setDescription('The IP address to which log messages are sent using the remote syslog facility.')
bnLogMsgRemoteSyslogSecondaryInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 17), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryInetAddressType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryInetAddressType.setDescription('The type of the IP address contained in the object bnLogMsgRemoteSyslogSecondaryInetAddress. Together, these two objects specify a second IP address to which log messages are sent using the remote syslog facility. If the value of this object is unknown(0), then messages are not sent to this address.')
bnLogMsgRemoteSyslogSecondaryInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 18), InetAddress().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryInetAddress.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryInetAddress.setDescription('The IP address to which log messages are sent using the remote syslog facility.')
bnLogMsgRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19), )
if mibBuilder.loadTexts: bnLogMsgRemoteServerTable.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerTable.setDescription('A table of remote logging server addresses.')
bnLogMsgRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1), ).setIndexNames((0, "BN-LOG-MESSAGE-MIB", "bnLogMsgRemoteServerAddressType"), (0, "BN-LOG-MESSAGE-MIB", "bnLogMsgRemoteServerAddress"))
if mibBuilder.loadTexts: bnLogMsgRemoteServerEntry.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerEntry.setDescription('A remote logging server address.')
bnLogMsgRemoteServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 1), InetAddressType())
if mibBuilder.loadTexts: bnLogMsgRemoteServerAddressType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerAddressType.setDescription('The type of address represented by this entry. The value of this object indicates the format of the value of the corresponding instance of bnLogMsgRemoteServerAddress. Currently only the values ipv4(1) and ipv6(2) are allowed for this object.')
bnLogMsgRemoteServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: bnLogMsgRemoteServerAddress.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerAddress.setDescription('The address represented by this entry.')
bnLogMsgRemoteServerEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bnLogMsgRemoteServerEnabled.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerEnabled.setDescription('Indicates whether this server is enabled.')
bnLogMsgRemoteServerSaveTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("msgTypeCritical", 1), ("msgTypeSerious", 2), ("msgTypeInformational", 3), ("msgTypeNone", 4))).clone('msgTypeCritical')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bnLogMsgRemoteServerSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerSaveTargets.setDescription("This object determines the type of log messages that will be sent to a remote syslog server when they occur. Messages are classified based on their type. Selecting a type value causes all log messages that have an associated value less than or equal to the type value specified to be sent when the log message is entered into the system. For example, specifying the value msgTypeCritical(1) causes only messages classified as 'critical' to be sent to the remote syslog server. Specifying msgTypeSerious(2) causes 'critical' and 'serious' messages to be sent. Specifying msgTypeNone(4) means that no log messages will be sent to the remote syslog server.")
bnLogMsgRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bnLogMsgRemoteServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerRowStatus.setDescription('This object is used to create/delete entries in this table.')
bnLogMsgRemoteServerStandardSaveTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 19, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("msgTypeEmergency", 0), ("msgTypeAlert", 1), ("msgTypeCritical", 2), ("msgTypeError", 3), ("msgTypeSerious", 4), ("msgTypeNotice", 5), ("msgTypeInformational", 6), ("msgTypeDebug", 7), ("msgTypeNone", 8))).clone('msgTypeNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bnLogMsgRemoteServerStandardSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteServerStandardSaveTargets.setDescription('This object determines the type of log messages that will be sent to a remote syslog server when they occur. Messages are classified based on their type. Selecting a type value causes all log messages that have an associated value less than or equal to the type value specified to be sent when the log message is entered into the system. ')
bnLogMsgRemoteSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("fltKernel", 1), ("fltUserLevel", 2), ("fltMailSystem", 3), ("fltDaemon", 4), ("fltSecAuthor", 5), ("fltMsgGenInt", 6), ("fltLinePrinter", 7), ("fltNetNews", 8), ("fltUUCP", 9), ("fltClockDaemon", 10), ("fltSecAuthor2", 11), ("fltFTPDaemon", 12), ("fltNTP", 13), ("fltLogAudit", 14), ("fltLogAlert", 15), ("fltClockDaemon2", 16), ("fltLocal0", 17), ("fltLocal1", 18), ("fltLocal2", 19), ("fltLocal3", 20), ("fltLocal4", 21), ("fltLocal5", 22), ("fltLocal6", 23), ("fltLocal7", 24), ("fltNone", 25))).clone('fltDaemon')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogFacility.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogFacility.setDescription('The facility against which remote logging is done.')
bnLogMsgRemoteSyslogStandardSaveTargets = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("msgTypeEmergency", 0), ("msgTypeAlert", 1), ("msgTypeCritical", 2), ("msgTypeError", 3), ("msgTypeSerious", 4), ("msgTypeNotice", 5), ("msgTypeInformational", 6), ("msgTypeDebug", 7), ("msgTypeNone", 8))).clone('msgTypeNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogStandardSaveTargets.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogStandardSaveTargets.setDescription('This object determines the type of log messages that will be sent to a remote syslog server when they occur. Messages are classified based on their type. Selecting a type value causes all log messages that have an associated value less than or equal to the type value specified to be sent when the log message is entered into the system.')
bnLogMsgRemoteSyslogPrimaryTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(601, 601), ValueRangeConstraint(1024, 65535), )).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogPrimaryTcpPort.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogPrimaryTcpPort.setDescription('Specifies the TCP port to use with the primary address for sending syslog messages to the host.')
bnLogMsgRemoteSyslogSecondaryTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(601, 601), ValueRangeConstraint(1024, 65535), )).clone(601)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryTcpPort.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryTcpPort.setDescription('Specifies the TCP port to use with the secondary address for sending syslog messages to the host.')
bnLogMsgRemoteSyslogPrimaryConnectionType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connectionTypeUDP", 1), ("connectionTypeTCP", 2), ("connectionTypeTCPSecure", 3))).clone('connectionTypeTCP')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogPrimaryConnectionType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogPrimaryConnectionType.setDescription('Specifies the primary connection type (TCP/UDP) to be used to send syslog messages to the host.')
bnLogMsgRemoteSyslogSecondaryConnectionType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connectionTypeUDP", 1), ("connectionTypeTCP", 2), ("connectionTypeTCPSecure", 3))).clone('connectionTypeTCP')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryConnectionType.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgRemoteSyslogSecondaryConnectionType.setDescription('Specifies the secondary connection type (TCP/UDP) to be used to send syslog messages to the host.')
bnLogMsgMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2, 0))
bnLogMsgBufferFull = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 16, 1, 2, 0, 1)).setObjects(("BN-LOG-MESSAGE-MIB", "bnLogMsgBufferCurSize"), ("BN-LOG-MESSAGE-MIB", "bnLogMsgBufferNonVolCurSize"))
if mibBuilder.loadTexts: bnLogMsgBufferFull.setStatus('current')
if mibBuilder.loadTexts: bnLogMsgBufferFull.setDescription('A bnLogMsgBufferFull trap is sent when either the volatile log message buffer space or the non-volatile log message buffer space is exhausted. An agent will generate this trap only once when it is determined that the buffer facilities are exhausted. This trap will not be sent again until the message storage facilities are cleared via the bnLogMsgBufferClearMsgs object. Note that, for example, clearing only the volatile storage space when the non-volatile space is full will result in another trap being generated when the non-volatile space is next found to be full (e.g., when the next log message to be saved in non-volatile storage is generated).')
mibBuilder.exportSymbols("BN-LOG-MESSAGE-MIB", bnLogMsgRemoteSyslogInetAddress=bnLogMsgRemoteSyslogInetAddress, bnLogMsgRemoteSyslogSecondaryInetAddress=bnLogMsgRemoteSyslogSecondaryInetAddress, bnLogMsgMIBTrapPrefix=bnLogMsgMIBTrapPrefix, bnLogMsgRemoteServerTable=bnLogMsgRemoteServerTable, bnLogMsgRemoteSyslogEnabled=bnLogMsgRemoteSyslogEnabled, bnLogMsgBufferMsgParam1=bnLogMsgBufferMsgParam1, bnLogMsgRemoteSyslogSecondaryInetAddressType=bnLogMsgRemoteSyslogSecondaryInetAddressType, bnLogMsgMIBConformance=bnLogMsgMIBConformance, PYSNMP_MODULE_ID=bnLogMsgMIB, bnLogMsgBufferEntry=bnLogMsgBufferEntry, bnLogMsgBufferMaxSize=bnLogMsgBufferMaxSize, bnLogMsgBufferMsgType=bnLogMsgBufferMsgType, bnLogMsgBufferCurSize=bnLogMsgBufferCurSize, bnLogMsgRemoteServerRowStatus=bnLogMsgRemoteServerRowStatus, bnLogMsgRemoteSyslogSecondaryConnectionType=bnLogMsgRemoteSyslogSecondaryConnectionType, bnLogMsgRemoteSyslogStandardSaveTargets=bnLogMsgRemoteSyslogStandardSaveTargets, bnLogMsgRemoteSyslogSaveTargets=bnLogMsgRemoteSyslogSaveTargets, bnLogMsgBufferMsgParam2=bnLogMsgBufferMsgParam2, bnLogMsgRemoteServerEnabled=bnLogMsgRemoteServerEnabled, bnLogMsgBufferTable=bnLogMsgBufferTable, bnLogMsgRemoteSyslogSecondaryTcpPort=bnLogMsgRemoteSyslogSecondaryTcpPort, bnLogMsgBufferMsgSrc=bnLogMsgBufferMsgSrc, bnLogMsgBufferFull=bnLogMsgBufferFull, bnLogMsgBufferNonVolSaveTargets=bnLogMsgBufferNonVolSaveTargets, bnLogMsgRemoteSyslogPrimaryConnectionType=bnLogMsgRemoteSyslogPrimaryConnectionType, bnLogMsgRemoteSyslogInetAddressType=bnLogMsgRemoteSyslogInetAddressType, bnLogMsgRemoteServerEntry=bnLogMsgRemoteServerEntry, bnLogMsgBufferMsgUtcTime=bnLogMsgBufferMsgUtcTime, bnLogMsgBufferFullAction=bnLogMsgBufferFullAction, bnLogMsgBufferClearMsgs=bnLogMsgBufferClearMsgs, bnLogMsgRemoteServerAddressType=bnLogMsgRemoteServerAddressType, bnLogMsgRemoteServerStandardSaveTargets=bnLogMsgRemoteServerStandardSaveTargets, bnLogMsgBufferOperaton=bnLogMsgBufferOperaton, bnLogMsgRemoteSyslogAddress=bnLogMsgRemoteSyslogAddress, bnLogMsgBufferNonVolCurSize=bnLogMsgBufferNonVolCurSize, bnLogMsgMIBObjects=bnLogMsgMIBObjects, bnLogMsgBufferMsgIndex=bnLogMsgBufferMsgIndex, bnLogMsgBufferMsgTime=bnLogMsgBufferMsgTime, bnLogMsgRemoteSyslogFacility=bnLogMsgRemoteSyslogFacility, bnLogMsgBufferSaveTargets=bnLogMsgBufferSaveTargets, bnLogMsgRemoteServerAddress=bnLogMsgRemoteServerAddress, bnLogMsgMIBTraps=bnLogMsgMIBTraps, bnLogMsgBufferMsgString=bnLogMsgBufferMsgString, bnLogMsgBufferMsgCode=bnLogMsgBufferMsgCode, bnLogMsgBufferMsgOrig=bnLogMsgBufferMsgOrig, bnLogMsgRemoteSyslogPrimaryTcpPort=bnLogMsgRemoteSyslogPrimaryTcpPort, bnLogMsgBufferClearTargets=bnLogMsgBufferClearTargets, bnLogMsgBufferMsgParam3=bnLogMsgBufferMsgParam3, bnLogMsgClearMessageBuffers=bnLogMsgClearMessageBuffers, bnLogMsgMIB=bnLogMsgMIB, bnLogMsgRemoteServerSaveTargets=bnLogMsgRemoteServerSaveTargets)