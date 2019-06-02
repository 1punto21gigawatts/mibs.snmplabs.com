#
# PySNMP MIB module SONUS-GATEWAY-SIGNALLING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-GATEWAY-SIGNALLING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Gauge32, iso, Counter32, ObjectIdentity, NotificationType, Bits, Counter64, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "Counter32", "ObjectIdentity", "NotificationType", "Bits", "Counter64", "TimeTicks", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
sonusEventClass, sonusEventDescription, sonusEventLevel = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusEventClass", "sonusEventDescription", "sonusEventLevel")
sonusSignallingMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSignallingMIBs")
SonusServiceState, SonusAdminState = mibBuilder.importSymbols("SONUS-TC", "SonusServiceState", "SonusAdminState")
sonusGatewaySignallingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2))
if mibBuilder.loadTexts: sonusGatewaySignallingMIB.setLastUpdated('200107310000Z')
if mibBuilder.loadTexts: sonusGatewaySignallingMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusGatewaySignallingMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusGatewaySignallingMIB.setDescription('The MIB Module for IP Call Signal Channel Management.')
sonusGatewaySignallingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1))
sonusGwSigTimerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1))
sonusGwSigSrvTimerT301 = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigSrvTimerT301.setStatus('obsolete')
if mibBuilder.loadTexts: sonusGwSigSrvTimerT301.setDescription('This is the gateway to gateway call establishment timer T301 (in seconds). This value applies to all future GW-GW calls.')
sonusGwSigSrvTimerT303 = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigSrvTimerT303.setStatus('obsolete')
if mibBuilder.loadTexts: sonusGwSigSrvTimerT303.setDescription('This is the gateway to gateway call setup timer T303 (in seconds). This value applies to all future GW-GW calls.')
sonusGwSigTimerEstabish = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigTimerEstabish.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigTimerEstabish.setDescription('This is the Gateway Signal Channel Establishment Timer (in seconds.) This value applies to all signal channels.')
sonusGwSigTimerKeepalive = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigTimerKeepalive.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigTimerKeepalive.setDescription('This is the Gateway Signal Channel Keepalive Timer (in seconds.) This value applies to all signal channels.')
sonusGwSigActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2))
sonusGwSigAction = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("close", 2), ("none", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigAction.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigAction.setDescription('The action to be taken on the specified link.')
sonusGwSigActionDestIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigActionDestIpAddr.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActionDestIpAddr.setDescription('The IP Address of the Destination Gateway to which the signalling link will be opened or closed.')
sonusGwSigActionDestPort = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(2569)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigActionDestPort.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActionDestPort.setDescription('The Port Number to which a call sig link will be opened.')
sonusGwSigActionDir = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("to", 1), ("from", 2), ("both", 3))).clone('to')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigActionDir.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActionDir.setDescription('The direction of the link which we will be opening or closing.')
sonusGwSigPortTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3), )
if mibBuilder.loadTexts: sonusGwSigPortTable.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortTable.setDescription('Table of Gateway Signal Listen Port configurations. Limit of two ports.')
sonusGwSigPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1), ).setIndexNames((0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigPortIndex"))
if mibBuilder.loadTexts: sonusGwSigPortEntry.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortEntry.setDescription('Gateway Signal Listen Port configuration.')
sonusGwSigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortIndex.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortIndex.setDescription('Identifies the Signal Listen Port entry.')
sonusGwSigPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortIpAddress.setDescription('IP Address of the Gateway Signal Listen Port - this is a required parameter.')
sonusGwSigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortNum.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortNum.setDescription('TCP port number of Gateway Signal Listen Port (default is Sonus registered port 2569).')
sonusGwSigPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgtNif", 1), ("nif", 2))).clone('mgtNif')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortInterface.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortInterface.setDescription("The interface type of Gateway Signal Listen Port. This element select which gateway network interfaces to use for GW-GW signaling traffic. 'mgtnif' routes traffic over the gateway Managment ports. 'nif' routes traffic over one of the gateway PNS ports.")
sonusGwSigPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortRole.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortRole.setDescription('Role of the Gateway Signal Listen Port.')
sonusGwSigPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 6), SonusServiceState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortMode.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortMode.setDescription('Mode of the Gateway Signal Listen Port.')
sonusGwSigPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 7), SonusAdminState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortState.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortState.setDescription('State of the Gateway Signal Listen Port.')
sonusGwSigPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 3, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusGwSigPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortRowStatus.setDescription('This is for SNMP use.')
sonusGwSigPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4), )
if mibBuilder.loadTexts: sonusGwSigPortStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatTable.setDescription('Table of the status of Gateway Signal Listen Ports.')
sonusGwSigPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1), ).setIndexNames((0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigPortStatIndex"))
if mibBuilder.loadTexts: sonusGwSigPortStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatEntry.setDescription('Status of Gateway Signal Listen Port.')
sonusGwSigPortStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatIndex.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatIndex.setDescription('Identifies the Signal Listen Port entry.')
sonusGwSigPortStatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatIpAddress.setDescription('IP Address of the Gateway Signal Listen Port.')
sonusGwSigPortStatNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatNum.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatNum.setDescription('TCP port number of Gateway Signal Listen Port.')
sonusGwSigPortStatInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgtNif", 1), ("nif", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatInterface.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatInterface.setDescription('The interface type of Gateway Signal Listen Port.')
sonusGwSigPortStatRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatRole.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatRole.setDescription('Role of the Gateway Signal Listen Port.')
sonusGwSigPortStatNif = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatNif.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatNif.setDescription('The network interface (NIF) ifIndex for this Gateway Signal Listen Port.')
sonusGwSigPortStatState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 4, 1, 7), SonusServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigPortStatState.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigPortStatState.setDescription('State of the Gateway Signal Listen Port.')
sonusGwSigActGwStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5), )
if mibBuilder.loadTexts: sonusGwSigActGwStatusTable.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwStatusTable.setDescription('This table contains status of the active signaling channels with other gateways.')
sonusGwSigActGwStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1), ).setIndexNames((0, "SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwSigActGwIpAddress"))
if mibBuilder.loadTexts: sonusGwSigActGwStatusEntry.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwStatusEntry.setDescription('Status of signaling channel another gateway.')
sonusGwSigActGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwName.setStatus('deprecated')
if mibBuilder.loadTexts: sonusGwSigActGwName.setDescription('Name of the remote Gateway.')
sonusGwSigActGwIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwIpAddress.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwIpAddress.setDescription('IP Address of the remote Gateway.')
sonusGwSigActGwLnkProto = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ioi", 1), ("h323", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwLnkProto.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwLnkProto.setDescription('The protocol being used between gateways.')
sonusGwSigActGwNumActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCalls.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCalls.setDescription('Number of active calls between local and remote Gateway.')
sonusGwSigActGwNumActiveCallsTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCallsTo.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCallsTo.setDescription('Number of active calls to this remote Gateway.')
sonusGwSigActGwNumActiveCallsFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCallsFrom.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwNumActiveCallsFrom.setDescription('Number of active calls from this remote Gateway.')
sonusGwSigActGwToState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 7), SonusServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToState.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToState.setDescription('Current state of the signaling link to this remote Gateway')
sonusGwSigActGwFromState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 8), SonusServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromState.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromState.setDescription('Current state of the signaling link from this remote Gateway')
sonusGwSigActGwInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgtNif", 1), ("nif", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwInterface.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwInterface.setDescription('The interface used for this link.')
sonusGwSigActGwFromBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromBytesSent.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromBytesSent.setDescription('The total number of signalling bytes sent to this remote Gateway for incoming calls')
sonusGwSigActGwFromPdusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromPdusSent.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromPdusSent.setDescription('The total number of signalling PDUS sent to this remote Gateway for incoming calls')
sonusGwSigActGwFromBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromBytesReceived.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromBytesReceived.setDescription('The total number of signalling bytes received from this remote Gateway for incoming calls')
sonusGwSigActGwFromPdusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromPdusReceived.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromPdusReceived.setDescription('The total number of signalling PDUS received from this remote Gateway for incoming calls')
sonusGwSigActGwFromTotalCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromTotalCalls.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromTotalCalls.setDescription('The total number of calls originated by the remote on this link ')
sonusGwSigActGwFromCallRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromCallRate.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromCallRate.setDescription('The number of calls/sec processed by the GWFE in the last minute on the link which was originated by the remote')
sonusGwSigActGwToBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToBytesSent.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToBytesSent.setDescription('The total number of signalling bytes sent to this remote Gateway for outgoing calls')
sonusGwSigActGwToPdusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToPdusSent.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToPdusSent.setDescription('The total number of signalling PDUS sent to this remote Gateway for outgoing calls')
sonusGwSigActGwToBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToBytesReceived.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToBytesReceived.setDescription('The total number of signalling bytes received from this remote Gateway for outgoing calls')
sonusGwSigActGwToPdusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToPdusReceived.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToPdusReceived.setDescription('The total number of signalling PDUS received from this remote Gateway for outgoing calls')
sonusGwSigActGwToTotalCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToTotalCalls.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToTotalCalls.setDescription('The total number of calls originated locally on this link ')
sonusGwSigActGwToCallRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToCallRate.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToCallRate.setDescription('The number of calls/sec processed by the GWFE in the last minute on the link which was originated locally')
sonusGwSigActGwFromLnkMajorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromLnkMajorVer.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromLnkMajorVer.setDescription('The major version of link protocol being used between gateways.')
sonusGwSigActGwFromLnkMinorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwFromLnkMinorVer.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwFromLnkMinorVer.setDescription('The minor version of link protocol being used between gateways.')
sonusGwSigActGwToLnkMajorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToLnkMajorVer.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToLnkMajorVer.setDescription('The major version of link protocol being used between gateways.')
sonusGwSigActGwToLnkMinorVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 1, 5, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwSigActGwToLnkMinorVer.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigActGwToLnkMinorVer.setDescription('The minor version of link protocol being used between gateways.')
sonusGatewaySignallingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2))
sonusGatewaySignallingMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0))
sonusGatewaySignallingMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1))
sonusGwRemoteGwName = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwRemoteGwName.setStatus('deprecated')
if mibBuilder.loadTexts: sonusGwRemoteGwName.setDescription('Name of the remote Gateway.')
sonusGwCloseReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("administratorInitiatedClose", 1), ("closeRequestReceivedFromRemote", 2), ("remoteNotResponding", 3), ("internalError", 4), ("configError", 5), ("recvCallSigReqFromUnknownGw", 6), ("socketErrNetworkDown", 7), ("socketErrNetworkUnreachable", 8), ("socketErrNetworkReset", 9), ("socketErrSoftwareConnectionAbort", 10), ("socketErrConnectionResetByPeer", 11), ("socketErrNoBufferSpaceAvail", 12), ("socketErrAlreadyConnected", 13), ("socketErrNotConnected", 14), ("socketErrCantSendAfterShutdown", 15), ("socketErrTooManyReferences", 16), ("socketErrConnectionTimedOut", 17), ("socketErrUnknown", 18), ("recvDuplicateLinkOpenReq", 19), ("socketErrExceptionEvent", 20), ("linkXmtCongestion", 21), ("openNackReceivedFromRemote", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwCloseReasonCode.setStatus('current')
if mibBuilder.loadTexts: sonusGwCloseReasonCode.setDescription('Reason for close of Call Signalling Channel .')
sonusGwRemoteGwAddr = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusGwRemoteGwAddr.setStatus('current')
if mibBuilder.loadTexts: sonusGwRemoteGwAddr.setDescription('Ip Address of the remote Gateway.')
sonusGwCallSigChanOpenNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 1)).setObjects(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwName"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusGwCallSigChanOpenNotification.setStatus('deprecated')
if mibBuilder.loadTexts: sonusGwCallSigChanOpenNotification.setDescription('This trap indicates that a Call Signalling channel to a Remote Gateway has been opened. This trap has been replaced with sonusGwSigChanOpenNotification.')
sonusGwCallSigChanCloseNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 2)).setObjects(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwName"), ("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwCloseReasonCode"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusGwCallSigChanCloseNotification.setStatus('deprecated')
if mibBuilder.loadTexts: sonusGwCallSigChanCloseNotification.setDescription('This trap indicates that a Call Signalling channel to a Remote Gateway has been closed. This trap has been replaced with sonusGwSigChanCloseNotification.')
sonusGwSigChanOpenNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 3)).setObjects(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwAddr"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusGwSigChanOpenNotification.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigChanOpenNotification.setDescription('This trap indicates that a Call Signalling channel to a Remote Gateway has been opened.')
sonusGwSigChanCloseNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 6, 2, 2, 0, 4)).setObjects(("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwRemoteGwAddr"), ("SONUS-GATEWAY-SIGNALLING-MIB", "sonusGwCloseReasonCode"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusGwSigChanCloseNotification.setStatus('current')
if mibBuilder.loadTexts: sonusGwSigChanCloseNotification.setDescription('This trap indicates that a Call Signalling channel to a Remote Gateway has been closed.')
mibBuilder.exportSymbols("SONUS-GATEWAY-SIGNALLING-MIB", sonusGwSigPortStatRole=sonusGwSigPortStatRole, sonusGwSigPortStatNum=sonusGwSigPortStatNum, sonusGwSigTimerEstabish=sonusGwSigTimerEstabish, sonusGwSigPortInterface=sonusGwSigPortInterface, sonusGwSigActGwLnkProto=sonusGwSigActGwLnkProto, sonusGwSigActGwNumActiveCallsTo=sonusGwSigActGwNumActiveCallsTo, sonusGwSigActGwFromPdusReceived=sonusGwSigActGwFromPdusReceived, sonusGwSigActGwInterface=sonusGwSigActGwInterface, sonusGwSigActGwToLnkMajorVer=sonusGwSigActGwToLnkMajorVer, PYSNMP_MODULE_ID=sonusGatewaySignallingMIB, sonusGwSigActionObjects=sonusGwSigActionObjects, sonusGwSigPortRole=sonusGwSigPortRole, sonusGwSigActGwStatusEntry=sonusGwSigActGwStatusEntry, sonusGatewaySignallingMIB=sonusGatewaySignallingMIB, sonusGwSigActGwStatusTable=sonusGwSigActGwStatusTable, sonusGwSigActGwNumActiveCalls=sonusGwSigActGwNumActiveCalls, sonusGwSigActGwToState=sonusGwSigActGwToState, sonusGwSigActionDestPort=sonusGwSigActionDestPort, sonusGatewaySignallingMIBNotificationsObjects=sonusGatewaySignallingMIBNotificationsObjects, sonusGwSigPortIpAddress=sonusGwSigPortIpAddress, sonusGwSigActGwFromState=sonusGwSigActGwFromState, sonusGwSigActGwFromLnkMajorVer=sonusGwSigActGwFromLnkMajorVer, sonusGwRemoteGwName=sonusGwRemoteGwName, sonusGwSigPortStatState=sonusGwSigPortStatState, sonusGwSigPortMode=sonusGwSigPortMode, sonusGwSigActGwToBytesReceived=sonusGwSigActGwToBytesReceived, sonusGwSigPortEntry=sonusGwSigPortEntry, sonusGwSigPortStatEntry=sonusGwSigPortStatEntry, sonusGwSigPortRowStatus=sonusGwSigPortRowStatus, sonusGwCloseReasonCode=sonusGwCloseReasonCode, sonusGwSigActGwToLnkMinorVer=sonusGwSigActGwToLnkMinorVer, sonusGwSigChanOpenNotification=sonusGwSigChanOpenNotification, sonusGwSigPortStatInterface=sonusGwSigPortStatInterface, sonusGwSigActGwToPdusReceived=sonusGwSigActGwToPdusReceived, sonusGwCallSigChanOpenNotification=sonusGwCallSigChanOpenNotification, sonusGwCallSigChanCloseNotification=sonusGwCallSigChanCloseNotification, sonusGwSigPortTable=sonusGwSigPortTable, sonusGwSigPortIndex=sonusGwSigPortIndex, sonusGatewaySignallingMIBObjects=sonusGatewaySignallingMIBObjects, sonusGwSigActGwIpAddress=sonusGwSigActGwIpAddress, sonusGwSigActionDestIpAddr=sonusGwSigActionDestIpAddr, sonusGwSigActGwNumActiveCallsFrom=sonusGwSigActGwNumActiveCallsFrom, sonusGwSigActGwFromPdusSent=sonusGwSigActGwFromPdusSent, sonusGwSigActGwFromTotalCalls=sonusGwSigActGwFromTotalCalls, sonusGwSigActGwToTotalCalls=sonusGwSigActGwToTotalCalls, sonusGwSigActGwToCallRate=sonusGwSigActGwToCallRate, sonusGwSigActionDir=sonusGwSigActionDir, sonusGwSigTimerKeepalive=sonusGwSigTimerKeepalive, sonusGwSigPortStatIpAddress=sonusGwSigPortStatIpAddress, sonusGwSigActGwName=sonusGwSigActGwName, sonusGwSigActGwFromCallRate=sonusGwSigActGwFromCallRate, sonusGatewaySignallingMIBNotifications=sonusGatewaySignallingMIBNotifications, sonusGwRemoteGwAddr=sonusGwRemoteGwAddr, sonusGwSigChanCloseNotification=sonusGwSigChanCloseNotification, sonusGwSigPortState=sonusGwSigPortState, sonusGatewaySignallingMIBNotificationsPrefix=sonusGatewaySignallingMIBNotificationsPrefix, sonusGwSigActGwToPdusSent=sonusGwSigActGwToPdusSent, sonusGwSigActGwFromLnkMinorVer=sonusGwSigActGwFromLnkMinorVer, sonusGwSigSrvTimerT303=sonusGwSigSrvTimerT303, sonusGwSigActGwFromBytesReceived=sonusGwSigActGwFromBytesReceived, sonusGwSigAction=sonusGwSigAction, sonusGwSigPortNum=sonusGwSigPortNum, sonusGwSigPortStatNif=sonusGwSigPortStatNif, sonusGwSigPortStatTable=sonusGwSigPortStatTable, sonusGwSigActGwFromBytesSent=sonusGwSigActGwFromBytesSent, sonusGwSigTimerObjects=sonusGwSigTimerObjects, sonusGwSigPortStatIndex=sonusGwSigPortStatIndex, sonusGwSigSrvTimerT301=sonusGwSigSrvTimerT301, sonusGwSigActGwToBytesSent=sonusGwSigActGwToBytesSent)