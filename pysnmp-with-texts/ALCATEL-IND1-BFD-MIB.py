#
# PySNMP MIB module ALCATEL-IND1-BFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-BFD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:17:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1BFD, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1BFD")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, TimeTicks, Bits, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Integer32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Integer32", "Counter32", "Counter64")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
alcatelIND1BfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1))
alcatelIND1BfdMIB.setRevisions(('2010-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1BfdMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1BfdMIB.setLastUpdated('201005050000Z')
if mibBuilder.loadTexts: alcatelIND1BfdMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1BfdMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1BfdMIB.setDescription('This document describes the Management Information Base for Bidirectional Forwarding Detection(BFD) Protocol. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alaBfdObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1))
if mibBuilder.loadTexts: alaBfdObjects.setStatus('current')
if mibBuilder.loadTexts: alaBfdObjects.setDescription('Branch for Bidirectional Forwarding Detection subsystem managed objects')
alcatelIND1BfdMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2))
if mibBuilder.loadTexts: alcatelIND1BfdMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1BfdMIBConformance.setDescription('Conformance')
class AlaBfdInterval(TextualConvention, Unsigned32):
    description = 'The BFD interval delay, in milliseconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class AlaBfdDiag(TextualConvention, Integer32):
    description = 'A common BFD diagnostic code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8))

class AlaBfdStatus(TextualConvention, Integer32):
    description = 'Administrative status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

alaBfdGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1))
alaBfdGlobalVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 1), Unsigned32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdGlobalVersionNumber.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalVersionNumber.setDescription('The version number of the BFD protocol that is used by BFD sessions in this router instance.')
alaBfdGlobalAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 2), AlaBfdStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaBfdGlobalAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalAdminStatus.setDescription('The administrative status of BFD in this router instance.')
alaBfdGlobalTxInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 3), AlaBfdInterval().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaBfdGlobalTxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalTxInterval.setDescription('The Desired Tx interval, in milliseconds, at which packets should be transmitted on BFD sessions in this router instance.')
alaBfdGlobalRxInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 4), AlaBfdInterval().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaBfdGlobalRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalRxInterval.setDescription('The Minimum Rx interval, in milliseconds, at which packets can be received on BFD sessions in this router instance.')
alaBfdGlobalDetectMult = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaBfdGlobalDetectMult.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalDetectMult.setDescription('The Detection time multiplier. The negotiated transmit interval, multiplied by the value of this object, provides the detection time for the receiving system.')
alaBfdGlobalEchoRxInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 6), AlaBfdInterval().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaBfdGlobalEchoRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalEchoRxInterval.setDescription('The Minimum Echo Rx interval, in milliseconds, at which packets can be received on BFD sessions in this router instance.')
alaBfdGlobalProtocolApps = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 7), Bits().clone(namedValues=NamedValues(("vrrp", 0), ("staticRtg", 1), ("ospf", 2), ("bgp", 3), ("isis", 4), ("pim", 5), ("dvmrp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdGlobalProtocolApps.setStatus('current')
if mibBuilder.loadTexts: alaBfdGlobalProtocolApps.setDescription('Bit map object to reflect BFD applications currently registered to request BFD session state notifications. Bits 0 - 6 are currently in use, and if set, indicate that the respective application is registered with BFD: bit 0 - VRRP bit 1 - STATIC ROUTING (i.e. IP Route Manager) bit 2 - OSPF bit 3 - BGP bit 4 - ISIS bit 5 - PIM bit 6 - DVMRP ')
alaBfdIntfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2), )
if mibBuilder.loadTexts: alaBfdIntfTable.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfTable.setDescription('The BFD Interface Table describes the configured parameters used for BFD sessions on this outgoing IP interface, identified by the interface index.')
alaBfdIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-BFD-MIB", "alaBfdIntfIndex"))
if mibBuilder.loadTexts: alaBfdIntfEntry.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfEntry.setDescription('The BFD interface Entry describes BFD session configuration for the IP interface.')
alaBfdIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: alaBfdIntfIndex.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfIndex.setDescription('The ifIndex of the IP Interface for which the BFD session configuration is applied')
alaBfdIntfAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfAddrType.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfAddrType.setDescription('This object specifies IP address type values - unknown(0), ipv4(1) or ipv6(2).')
alaBfdIntfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfAddr.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfAddr.setDescription('The address of the IP interface for which BFD session parameters are configured')
alaBfdIntfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 4), AlaBfdStatus().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfAdminStatus.setDescription('The administrative status of the BFD interface.')
alaBfdIntfDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 5), AlaBfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfDesiredMinTxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfDesiredMinTxInterval.setDescription('The Minimum Desired Tx interval at which packets should be transmitted for BFD sessions on this interface. The default value for this object is derived from the value of alaBfdGlobalTxInterval.')
alaBfdIntfReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 6), AlaBfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfReqMinRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfReqMinRxInterval.setDescription('The Minimum Rx interval at which packets can be received for BFD sessions on this interface. The default value for this object is derived from the value of alaBfdGlobalRxInterval.')
alaBfdIntfReqMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 7), AlaBfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfReqMinEchoRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfReqMinEchoRxInterval.setDescription('The Minimum Echo Rx interval at which ECHO packets can be received for BFD sessions on this interface. The default value for this object is derived from the value of alaBfdGlobalEchoRxInterval.')
alaBfdIntfDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfDetectMult.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfDetectMult.setDescription('The Detection time multiplier for BFD sessions on this interface. The default value for this object is derived from the value of alaBfdGlobalDetectMult.')
alaBfdIntfAuthPresFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfAuthPresFlag.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfAuthPresFlag.setDescription("This object indicates the local system's desire to use authentication on BFD sessions. If set to true(1), the local system wishes the session to be authenticated and set to false(0) if not.")
alaBfdIntfAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("simplePassword", 2), ("keyedMD5", 3), ("meticulousKeyedMD5", 4), ("keyedSHA1", 5), ("meticulousKeyedSHA1", 6))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfAuthenticationType.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfAuthenticationType.setDescription('The Authentication Type used for BFD sessions on this interface. This field is valid only when the Authentication Present bit is set.')
alaBfdIntfIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 11), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfIfName.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfIfName.setDescription('The user defined name used to identify the IP interface')
alaBfdIntfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfOperStatus.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfOperStatus.setDescription('The operational status of this BFD IP interface, which is dependent on IP interface status.')
alaBfdIntfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaBfdIntfRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfRowStatus.setDescription('Snmp row status variable for this interface entry.')
alaBfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3), )
if mibBuilder.loadTexts: alaBfdSessTable.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessTable.setDescription('The BFD Session Table describes the BFD sessions for this router instance.')
alaBfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-BFD-MIB", "alaBfdSessDiscriminator"))
if mibBuilder.loadTexts: alaBfdSessEntry.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessEntry.setDescription('The BFD Session Entry describes the BFD session.')
alaBfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: alaBfdSessDiscriminator.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessDiscriminator.setDescription('The systemwide-unique local discriminator that identifies this BFD session.')
alaBfdSessNeighborAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessNeighborAddrType.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessNeighborAddrType.setDescription('This object specifies the IP address type of the neighbor or remote router.')
alaBfdSessNeighborAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessNeighborAddr.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessNeighborAddr.setDescription('The IP address of the neighbor or remote router for this BFD session.')
alaBfdSessSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 4), Bits().clone(namedValues=NamedValues(("asynchronous", 0), ("echo", 1), ("demand", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessSessionType.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessSessionType.setDescription("This bit map object specifies the session type(s) that have been requested by BFD applications to this session's remote address. One or more applications can request different types of sessions to the same remote address. Bits 0 - 2 are currently in use, and if set, indicate that the respective session type has been requested for this session: bit 0 - Asynchronous bit 1 - Echo Function bit 2 - Demand ")
alaBfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessRemoteDiscr.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessRemoteDiscr.setDescription('The discriminator used by the remote router for this BFD session.')
alaBfdSessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessUdpPort.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessUdpPort.setDescription('The unique source UDP Port for this BFD session in this router instance.')
alaBfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessState.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessState.setDescription('The protocol state of the BFD session.')
alaBfdSessDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 8), AlaBfdDiag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessDiag.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessDiag.setDescription("A diagnostic code specifying the local system's reason for the last transition of the session from up(4)to some other state.")
alaBfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4), ("echoOnly", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessOperMode.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessOperMode.setDescription('This object specifies the current operating mode of the BFD session.')
alaBfdSessControlPlanIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessControlPlanIndepFlag.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessControlPlanIndepFlag.setDescription("This object indicates the local system's ability to continue to function through a disruption of the control plane. Specifically, it is set to true(1) if the local system's BFD implementation independent of the control plane. Otherwise, the value is set to false(0)")
alaBfdSessIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 12), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessIfIndex.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessIfIndex.setDescription('This object contains an ifIndex of the IP interface on which this BFD session is running. This value can be zero if there are no interface associated with this BFD session.')
alaBfdSessNegotiatedTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 13), AlaBfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessNegotiatedTxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessNegotiatedTxInterval.setDescription('This object specifies the minimum interval, in milliseconds, that the local system will transmit BFD Control packets.')
alaBfdSessNegotiatedRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 14), AlaBfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessNegotiatedRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessNegotiatedRxInterval.setDescription('This object specifies the minimum interval, in milliseconds, that the local system will receive BFD Control packets.')
alaBfdSessEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 15), AlaBfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessEchoRxInterval.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessEchoRxInterval.setDescription('This object specifies the minimum echo rx interval, in milliseconds, that the local system will receive BFD Echo packets.')
alaBfdSessProtocolApps = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 16), Bits().clone(namedValues=NamedValues(("vrrp", 0), ("staticRtg", 1), ("ospf", 2), ("bgp", 3), ("isis", 4), ("pim", 5), ("dvmrp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessProtocolApps.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessProtocolApps.setDescription("Bit map object to reflect BFD applications that have requested for detection to this session's remote address. Bits 0 - 6 are currently in use, and if set, indicate that the respective application has requested BFD session state event notifications: bit 0 - VRRP bit 1 - STATIC ROUTING (i.e. IP Route Manager) bit 2 - OSPF bit 3 - BGP bit 4 - ISIS bit 5 - PIM bit 6 - DVMRP ")
alaBfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4), )
if mibBuilder.loadTexts: alaBfdSessPerfTable.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfTable.setDescription('This table specifies BFD Session performance and statistics.')
alaBfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1), )
alaBfdSessEntry.registerAugmentions(("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEntry"))
alaBfdSessPerfEntry.setIndexNames(*alaBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: alaBfdSessPerfEntry.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfEntry.setDescription('An entry in this table is created for every BFD Session in this router instance.')
alaBfdSessPerfPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfPktIn.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfPktIn.setDescription('The total number of BFD packets received for this BFD session.')
alaBfdSessPerfPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfPktOut.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfPktOut.setDescription('The total number of BFD packets sent for this BFD session.')
alaBfdSessPerfEchoOut = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfEchoOut.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfEchoOut.setDescription('The total number of BFD Echo packets sent for this BFD session.')
alaBfdSessPerfEchoIn = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfEchoIn.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfEchoIn.setDescription('The total number of BFD Echo packets received for this BFD session.')
alaBfdSessPerfUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfUpTime.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfUpTime.setDescription('The system time elapsed since the most recent occasion at which the session became up. If no such event occured, this object contains a zero value.')
alaBfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfLastSessDownTime.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfLastSessDownTime.setDescription('The system time elapsed since the most recent occasion at which communication was lost with the remote end (i.e. session was down). If no such event occured, this object contains a zero value.')
alaBfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 7), AlaBfdDiag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfLastCommLostDiag.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfLastCommLostDiag.setDescription('The BFD diagnostic code for the last time communication was lost with the remote end. If no such event occured, this object contains a zero value.')
alaBfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfSessUpCount.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfSessUpCount.setDescription('The number of times this session has gone into the Up state since the router last rebooted.')
alaBfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaBfdSessPerfDiscTime.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfDiscTime.setDescription('The value of system time on the most recent occasion at which any one or more of the session counters suffered a discontinuity.The relevant counters are the specific instances associated with this BFD session of any Counter64 object contained in the BfdSessPerfTable. If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this object contains a zero value.')
alcatelIND1BfdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1))
alcatelIND1BfdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 2))
alcatelIND1BfdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-BFD-MIB", "alaBfdBasicGroup"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfCfgGroup"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessGroup"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1BfdMIBCompliance = alcatelIND1BfdMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1BfdMIBCompliance.setDescription('The compliance statement for device support of BFD.')
alaBfdBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalVersionNumber"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalAdminStatus"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalTxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalDetectMult"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalEchoRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalProtocolApps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaBfdBasicGroup = alaBfdBasicGroup.setStatus('current')
if mibBuilder.loadTexts: alaBfdBasicGroup.setDescription('A collection of objects providing information about the configuration done for BFD at global level.')
alaBfdIntfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddr"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddrType"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAdminStatus"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDesiredMinTxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinEchoRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDetectMult"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthPresFlag"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthenticationType"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfIfName"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfOperStatus"), ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaBfdIntfCfgGroup = alaBfdIntfCfgGroup.setStatus('current')
if mibBuilder.loadTexts: alaBfdIntfCfgGroup.setDescription('A collection of objects providing information about the configuration done for a BFD interface.')
alaBfdSessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddrType"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddr"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessSessionType"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessRemoteDiscr"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessUdpPort"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessState"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessDiag"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessOperMode"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessControlPlanIndepFlag"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessIfIndex"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedTxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessEchoRxInterval"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessProtocolApps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaBfdSessGroup = alaBfdSessGroup.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessGroup.setDescription('A collection of objects providing information about the BFD session.')
alaBfdSessPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktIn"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktOut"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEchoOut"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEchoIn"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfUpTime"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastSessDownTime"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastCommLostDiag"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfSessUpCount"), ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaBfdSessPerfGroup = alaBfdSessPerfGroup.setStatus('current')
if mibBuilder.loadTexts: alaBfdSessPerfGroup.setDescription('A collection of objects providing information about the BFD session performance counters.')
mibBuilder.exportSymbols("ALCATEL-IND1-BFD-MIB", alaBfdIntfIndex=alaBfdIntfIndex, alcatelIND1BfdMIB=alcatelIND1BfdMIB, alaBfdIntfRowStatus=alaBfdIntfRowStatus, AlaBfdDiag=AlaBfdDiag, alaBfdSessNeighborAddr=alaBfdSessNeighborAddr, alaBfdSessEchoRxInterval=alaBfdSessEchoRxInterval, alaBfdSessPerfPktIn=alaBfdSessPerfPktIn, alaBfdGlobalEchoRxInterval=alaBfdGlobalEchoRxInterval, alaBfdSessRemoteDiscr=alaBfdSessRemoteDiscr, alaBfdSessControlPlanIndepFlag=alaBfdSessControlPlanIndepFlag, alaBfdSessPerfPktOut=alaBfdSessPerfPktOut, alaBfdSessPerfEchoOut=alaBfdSessPerfEchoOut, alaBfdIntfEntry=alaBfdIntfEntry, alaBfdBasicGroup=alaBfdBasicGroup, alaBfdSessPerfEntry=alaBfdSessPerfEntry, alaBfdSessNegotiatedRxInterval=alaBfdSessNegotiatedRxInterval, alaBfdObjects=alaBfdObjects, alaBfdIntfDetectMult=alaBfdIntfDetectMult, alcatelIND1BfdMIBCompliance=alcatelIND1BfdMIBCompliance, alaBfdSessPerfDiscTime=alaBfdSessPerfDiscTime, alcatelIND1BfdMIBCompliances=alcatelIND1BfdMIBCompliances, alaBfdSessEntry=alaBfdSessEntry, alaBfdGlobalProtocolApps=alaBfdGlobalProtocolApps, alaBfdGlobalObjects=alaBfdGlobalObjects, alaBfdGlobalDetectMult=alaBfdGlobalDetectMult, alaBfdSessPerfTable=alaBfdSessPerfTable, AlaBfdInterval=AlaBfdInterval, alaBfdSessPerfEchoIn=alaBfdSessPerfEchoIn, alaBfdSessPerfUpTime=alaBfdSessPerfUpTime, alaBfdIntfDesiredMinTxInterval=alaBfdIntfDesiredMinTxInterval, alaBfdSessSessionType=alaBfdSessSessionType, alaBfdIntfOperStatus=alaBfdIntfOperStatus, alaBfdGlobalTxInterval=alaBfdGlobalTxInterval, PYSNMP_MODULE_ID=alcatelIND1BfdMIB, alaBfdGlobalAdminStatus=alaBfdGlobalAdminStatus, alaBfdSessPerfLastSessDownTime=alaBfdSessPerfLastSessDownTime, alaBfdIntfReqMinEchoRxInterval=alaBfdIntfReqMinEchoRxInterval, alcatelIND1BfdMIBConformance=alcatelIND1BfdMIBConformance, alaBfdGlobalVersionNumber=alaBfdGlobalVersionNumber, alaBfdSessPerfSessUpCount=alaBfdSessPerfSessUpCount, alaBfdIntfReqMinRxInterval=alaBfdIntfReqMinRxInterval, alaBfdIntfIfName=alaBfdIntfIfName, alaBfdSessPerfLastCommLostDiag=alaBfdSessPerfLastCommLostDiag, alaBfdSessNegotiatedTxInterval=alaBfdSessNegotiatedTxInterval, alaBfdSessOperMode=alaBfdSessOperMode, alaBfdSessProtocolApps=alaBfdSessProtocolApps, alaBfdIntfAddrType=alaBfdIntfAddrType, alaBfdIntfAuthenticationType=alaBfdIntfAuthenticationType, alaBfdSessUdpPort=alaBfdSessUdpPort, alaBfdSessIfIndex=alaBfdSessIfIndex, alaBfdIntfAuthPresFlag=alaBfdIntfAuthPresFlag, alaBfdSessGroup=alaBfdSessGroup, alaBfdSessPerfGroup=alaBfdSessPerfGroup, alaBfdSessNeighborAddrType=alaBfdSessNeighborAddrType, alaBfdIntfAdminStatus=alaBfdIntfAdminStatus, alaBfdSessDiag=alaBfdSessDiag, alaBfdIntfCfgGroup=alaBfdIntfCfgGroup, AlaBfdStatus=AlaBfdStatus, alaBfdSessTable=alaBfdSessTable, alaBfdSessDiscriminator=alaBfdSessDiscriminator, alaBfdIntfTable=alaBfdIntfTable, alaBfdSessState=alaBfdSessState, alcatelIND1BfdMIBGroups=alcatelIND1BfdMIBGroups, alaBfdGlobalRxInterval=alaBfdGlobalRxInterval, alaBfdIntfAddr=alaBfdIntfAddr)