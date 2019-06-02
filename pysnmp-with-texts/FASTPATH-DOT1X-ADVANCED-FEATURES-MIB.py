#
# PySNMP MIB module FASTPATH-DOT1X-ADVANCED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-DOT1X-ADVANCED-FEATURES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter64, Gauge32, Counter32, IpAddress, iso, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter64", "Gauge32", "Counter32", "IpAddress", "iso", "TimeTicks", "MibIdentifier")
RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
fastPathdot1xAdvanced = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36))
fastPathdot1xAdvanced.setRevisions(('2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathdot1xAdvanced.setRevisionsDescriptions(('Broadcom branding related changes.',))
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setContactInfo(' Customer Support Postal: Broadcom Corporation 100, Perimeter Park Drive Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathdot1xAdvanced.setDescription('The Broadcom Private MIB for FastPath Dot1x Advanced Features ')
class Dot1xPortControlMode(TextualConvention, Integer32):
    description = 'The control values of the Authenticator PAE controlled Port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3), ("macBased", 4))

class Dot1xSessionTerminationAction(TextualConvention, Integer32):
    description = 'The action to be taken on session termination .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("reauthenticate", 2))

agentDot1xEnhancementConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1))
agentDot1xRadiusVlanAssignment = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xRadiusVlanAssignment.setStatus('current')
if mibBuilder.loadTexts: agentDot1xRadiusVlanAssignment.setDescription('Enable/Disable dot1x Vlan Assignment Support on the switch.')
agentDot1xPortConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2))
agentDot1xPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1), )
if mibBuilder.loadTexts: agentDot1xPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortConfigTable.setDescription('A table for dot1x enhanced Port details and associated functionality.')
agentDot1xPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: agentDot1xPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortConfigEntry.setDescription('Represents entry for port config table.')
agentDot1xPortControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 1), Dot1xPortControlMode().clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xPortControlMode.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortControlMode.setDescription('Dot1x port control mode of this port.The Port control mode . The port control mode for this interface can take the following values , force-unauthorized - the port is in unauthorized mode, auto-Port based mode. If a client authenticates suscessfully, then the interface is authorized . Otherwise, the port is in unauthorized mode. If more than one clients are attached to the port , then only one client needs to authenticate to allow other clients access. force-authorized - The port is placed in authorized mode macBased - If more than one client is attached to the port, then each client needs to authenticate separately. This object depcreates dot1xAuthAuthControlledPortControl object in IEEE8021-PAE-MIB')
agentDot1xGuestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanId.setStatus('current')
if mibBuilder.loadTexts: agentDot1xGuestVlanId.setDescription('Specifies the Guest Vlan of the port. A port will be moved to its Guest Vlan if no client sucessfully authenticates on that port for the Guest Vlan Period. A value of zero indicates no Guest Vlan is configured for the interface.')
agentDot1xGuestVlanPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanPeriod.setStatus('current')
if mibBuilder.loadTexts: agentDot1xGuestVlanPeriod.setDescription('The value, in seconds, of the guestVlanPeriod constant currently in use for Guest Vlan Assignment for the port .')
agentDot1xUnauthenticatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xUnauthenticatedVlan.setStatus('current')
if mibBuilder.loadTexts: agentDot1xUnauthenticatedVlan.setDescription('Specifies the Unauthenticated Vlan of the port. A port will be moved to its unauthenticated Vlan if the client authenticates unsucessfully on that port . A value of zero indicates no Unauthenticated Vlan is configured for the port. ')
agentDot1xMaxUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xMaxUsers.setStatus('current')
if mibBuilder.loadTexts: agentDot1xMaxUsers.setDescription(' Specifies the maximum users or clients that can authenticate on this port when the port control mode is macBased. ')
agentDot1xPortVlanAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortVlanAssigned.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortVlanAssigned.setDescription(' Specifies the vlan the port is assigned to by Dot1x . Only relevant if the port control mode of the port is auto. ')
agentDot1xPortVlanAssignedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("default", 1), ("radius", 2), ("unauthenticatedVlan", 3), ("guestVlan", 4), ("notAssigned", 5))).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortVlanAssignedReason.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortVlanAssignedReason.setDescription(' Reason the port is assigned to the vlan specified by agentDot1xPortVlanAssigned . Only relevant if the port control mode of the port is auto. ')
agentDot1xPortSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortSessionTimeout.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortSessionTimeout.setDescription(' Specifies the session timeout value assigned by the Radius server for this port . Only relevant if the port control mode of the port is auto. ')
agentDot1xPortTerminationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 9), Dot1xSessionTerminationAction().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortTerminationAction.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortTerminationAction.setDescription(' Specifies the session termination action assigned by the Radius Server .This is the action taken when the session times out . Only relevant if the port control mode of the port is auto. ')
agentDot1xPortMABenabled = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xPortMABenabled.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortMABenabled.setDescription(' Specifies if Mac-based bypass authentication is configured for the port. ')
agentDot1xPortMABenabledOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xPortMABenabledOperational.setStatus('current')
if mibBuilder.loadTexts: agentDot1xPortMABenabledOperational.setDescription(' Displays the operational value of the Mac-based authentication bypass mode (MAB) on the port. ')
agentDot1xClientConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3))
agentDot1xClientConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1), )
if mibBuilder.loadTexts: agentDot1xClientConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientConfigTable.setDescription('A table for dot1x Client details and associated functionality.')
agentDot1xClientConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1), ).setIndexNames((0, "FASTPATH-DOT1X-ADVANCED-FEATURES-MIB", "agentDot1xClientMacAddress"))
if mibBuilder.loadTexts: agentDot1xClientConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientConfigEntry.setDescription('Represents entry for port config table.')
agentDot1xClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientMacAddress.setDescription('Specifies the client MAC address of the client. ')
agentDot1xLogicalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xLogicalPort.setStatus('current')
if mibBuilder.loadTexts: agentDot1xLogicalPort.setDescription('Specifies the client MAC address of the client . ')
agentDot1xInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xInterface.setStatus('current')
if mibBuilder.loadTexts: agentDot1xInterface.setDescription('Specifies the physical interface to which the client is attached . ')
agentDot1xClientAuthPAEstate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientAuthPAEstate.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientAuthPAEstate.setDescription('The current value of the Authenticator PAE state machine for the client.')
agentDot1xClientBackendState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientBackendState.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientBackendState.setDescription('The current state of the Backend Authentication state machine.')
agentDot1xClientUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientUserName.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientUserName.setDescription('Specifies the username with which the client is authenticated to the Radius server . This value is only valid when the client is in authenticated state. ')
agentDot1xClientSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTime.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientSessionTime.setDescription('Specifies the time elapsed in seconds since the client was authenticated in this session. This value is only valid when the client is in authenticated state. ')
agentDot1xClientFilterID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientFilterID.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientFilterID.setDescription('Specifies the Filter ID or Diffserv Policy name to be applied to the session . This vlaue is populated only if it has been assigned by the RADIUS server. This value is only valid when the client is in authenticated state.')
agentDot1xClientVlanAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanAssigned.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientVlanAssigned.setDescription('Specifies the vlan the client is associated with by Dot1x . This value is only valid when the client is in authenticated state.')
agentDot1xClientVlanAssignedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("default", 1), ("radius", 2), ("unauthenticatedVlan", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanAssignedReason.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientVlanAssignedReason.setDescription(' Reason the client is associated to the vlan specified by agentDot1xClientVlanAssigned . This value is only valid when the client is in authenticated state.')
agentDot1xClientSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTimeout.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientSessionTimeout.setDescription('Specifies the session time remaining for the client if assigned by the Radius server . A value of 0 indicates that no session timeout was assigned by the RADIUS server. This value is only valid when the client is in authenticated state. ')
agentDot1xClientTerminationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 36, 3, 1, 1, 12), Dot1xSessionTerminationAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientTerminationAction.setStatus('current')
if mibBuilder.loadTexts: agentDot1xClientTerminationAction.setDescription('Specifies the session termination action assigned by the Radius Server . This is the action taken when the session times out . This value is only valid when the client is in authenticated state. ')
mibBuilder.exportSymbols("FASTPATH-DOT1X-ADVANCED-FEATURES-MIB", agentDot1xClientSessionTime=agentDot1xClientSessionTime, agentDot1xPortTerminationAction=agentDot1xPortTerminationAction, agentDot1xClientFilterID=agentDot1xClientFilterID, agentDot1xClientAuthPAEstate=agentDot1xClientAuthPAEstate, agentDot1xGuestVlanId=agentDot1xGuestVlanId, agentDot1xRadiusVlanAssignment=agentDot1xRadiusVlanAssignment, agentDot1xClientConfigGroup=agentDot1xClientConfigGroup, agentDot1xClientBackendState=agentDot1xClientBackendState, agentDot1xLogicalPort=agentDot1xLogicalPort, PYSNMP_MODULE_ID=fastPathdot1xAdvanced, agentDot1xClientConfigEntry=agentDot1xClientConfigEntry, agentDot1xPortVlanAssignedReason=agentDot1xPortVlanAssignedReason, agentDot1xPortConfigGroup=agentDot1xPortConfigGroup, agentDot1xClientConfigTable=agentDot1xClientConfigTable, agentDot1xInterface=agentDot1xInterface, agentDot1xPortSessionTimeout=agentDot1xPortSessionTimeout, agentDot1xPortConfigTable=agentDot1xPortConfigTable, agentDot1xGuestVlanPeriod=agentDot1xGuestVlanPeriod, Dot1xPortControlMode=Dot1xPortControlMode, agentDot1xPortConfigEntry=agentDot1xPortConfigEntry, agentDot1xPortMABenabled=agentDot1xPortMABenabled, agentDot1xClientVlanAssignedReason=agentDot1xClientVlanAssignedReason, agentDot1xClientSessionTimeout=agentDot1xClientSessionTimeout, agentDot1xUnauthenticatedVlan=agentDot1xUnauthenticatedVlan, agentDot1xClientUserName=agentDot1xClientUserName, agentDot1xPortControlMode=agentDot1xPortControlMode, agentDot1xClientTerminationAction=agentDot1xClientTerminationAction, Dot1xSessionTerminationAction=Dot1xSessionTerminationAction, agentDot1xClientMacAddress=agentDot1xClientMacAddress, fastPathdot1xAdvanced=fastPathdot1xAdvanced, agentDot1xPortVlanAssigned=agentDot1xPortVlanAssigned, agentDot1xClientVlanAssigned=agentDot1xClientVlanAssigned, agentDot1xEnhancementConfigGroup=agentDot1xEnhancementConfigGroup, agentDot1xMaxUsers=agentDot1xMaxUsers, agentDot1xPortMABenabledOperational=agentDot1xPortMABenabledOperational)