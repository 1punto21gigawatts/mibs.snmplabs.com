#
# PySNMP MIB module Wellfleet-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-TELNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, Gauge32, Unsigned32, Bits, IpAddress, ModuleIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Gauge32", "Unsigned32", "Bits", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfTelnetGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfTelnetGroup")
wfTelnet = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1))
wfTelnetDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete TELNET.')
wfTelnetDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDisable.setDescription('Enables or Disables TELNET Subsystem')
wfTelnetLinesPerScreen = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 3), Integer32().clone(24)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetLinesPerScreen.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetLinesPerScreen.setDescription('Number of lines which can be displayed in one screen on the Telnet Technician Interface console. (Default value if NAWS option not negotiated)')
wfTelnetMoreDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetMoreDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetMoreDisable.setDescription("Enable the 'more' feature on the Telnet Technician Interface console")
wfTelnetPrompt = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetPrompt.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetPrompt.setDescription('Character string which will be used as the system prompt on the Telnet Technician Interface console')
wfTelnetLoginTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetLoginTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetLoginTimeOut.setDescription('Time out in minutes to Disconnect when at the login prompt')
wfTelnetPasswordTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetPasswordTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetPasswordTimeOut.setDescription('Timout in minutes on Password entry')
wfTelnetCommandTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetCommandTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetCommandTimeOut.setDescription('Time out in minutes to Disconnect when at the command prompt')
wfTelnetLoginRetries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetLoginRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetLoginRetries.setDescription('Limit # of login attempts then Disconnect')
wfTelnetTotalLogins = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetTotalLogins.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetTotalLogins.setDescription('Total number of Telnet TI login attempts')
wfTelnetUserLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetUserLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetUserLoginErrors.setDescription('Total number of FAILED User login attempts')
wfTelnetManagerLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetManagerLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetManagerLoginErrors.setDescription('Total number of FAILED Manager login attempts')
wfTelnetOtherLoginErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetOtherLoginErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetOtherLoginErrors.setDescription('Total number of FAILED Other login attempts')
wfTelnetActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetActiveSessions.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetActiveSessions.setDescription('Total number of Telnet TI Sessions')
wfTelnetDiagnosticReport = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDiagnosticReport.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDiagnosticReport.setDescription('Diagnostic Flag: report prints the options information, plus some additional information about what processing is going on')
wfTelnetDiagnosticExercise = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDiagnosticExercise.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDiagnosticExercise.setDescription('Diagnostic Flag: Not implemented yet.')
wfTelnetDiagnosticNetworkData = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDiagnosticNetworkData.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDiagnosticNetworkData.setDescription('Diagnostic Flag: NETDATA displays the data stream received by telnetd')
wfTelnetDiagnosticPtyData = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDiagnosticPtyData.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDiagnosticPtyData.setDescription('Diagnostic Flag: PTYDATA displays data written to the pty')
wfTelnetDiagnosticOptions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetDiagnosticOptions.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetDiagnosticOptions.setDescription('Diagnostic Flag: OPTIONS prints information about the negotiation of TELNET options')
wfTelnetInitialSearchPath = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetInitialSearchPath.setStatus('obsolete')
if mibBuilder.loadTexts: wfTelnetInitialSearchPath.setDescription("Example: 'A:;1:;2:' or '2:;4:6:;9:")
wfTelnetManagerAutoScript = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetManagerAutoScript.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetManagerAutoScript.setDescription('for each login.')
wfTelnetUserAutoScript = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 22), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetUserAutoScript.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetUserAutoScript.setDescription('for each login.')
wfTelnetUserAbortLogoutDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetUserAbortLogoutDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetUserAbortLogoutDisable.setDescription('a USER from escaping out of the User Autoscript')
wfTelnetHistoryDepth = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetHistoryDepth.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetHistoryDepth.setDescription('TI command history table size')
wfTelnetReverseEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetReverseEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetReverseEnable.setDescription('Reverse Telnet enabled')
wfTelnetReversePort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetReversePort.setStatus('mandatory')
if mibBuilder.loadTexts: wfTelnetReversePort.setDescription('Console port to use for reverse telnet')
mibBuilder.exportSymbols("Wellfleet-TELNET-MIB", wfTelnetManagerAutoScript=wfTelnetManagerAutoScript, wfTelnetReverseEnable=wfTelnetReverseEnable, wfTelnetUserAbortLogoutDisable=wfTelnetUserAbortLogoutDisable, wfTelnetHistoryDepth=wfTelnetHistoryDepth, wfTelnetUserLoginErrors=wfTelnetUserLoginErrors, wfTelnetReversePort=wfTelnetReversePort, wfTelnetDiagnosticExercise=wfTelnetDiagnosticExercise, wfTelnetDiagnosticReport=wfTelnetDiagnosticReport, wfTelnetMoreDisable=wfTelnetMoreDisable, wfTelnetActiveSessions=wfTelnetActiveSessions, wfTelnetLoginTimeOut=wfTelnetLoginTimeOut, wfTelnetManagerLoginErrors=wfTelnetManagerLoginErrors, wfTelnetDiagnosticOptions=wfTelnetDiagnosticOptions, wfTelnetCommandTimeOut=wfTelnetCommandTimeOut, wfTelnetPasswordTimeOut=wfTelnetPasswordTimeOut, wfTelnetUserAutoScript=wfTelnetUserAutoScript, wfTelnetInitialSearchPath=wfTelnetInitialSearchPath, wfTelnetDelete=wfTelnetDelete, wfTelnetDiagnosticNetworkData=wfTelnetDiagnosticNetworkData, wfTelnetDiagnosticPtyData=wfTelnetDiagnosticPtyData, wfTelnetPrompt=wfTelnetPrompt, wfTelnetLinesPerScreen=wfTelnetLinesPerScreen, wfTelnetTotalLogins=wfTelnetTotalLogins, wfTelnetDisable=wfTelnetDisable, wfTelnetLoginRetries=wfTelnetLoginRetries, wfTelnet=wfTelnet, wfTelnetOtherLoginErrors=wfTelnetOtherLoginErrors)