#
# PySNMP MIB module CNT246-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNT246-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, Bits, MibIdentifier, NotificationType, Counter64, Counter32, Gauge32, ModuleIdentity, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "Bits", "MibIdentifier", "NotificationType", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cnt2Transport = ModuleIdentity((1, 3, 6, 1, 4, 1, 333, 2, 4, 6))
cnt2Transport.setRevisions(('1901-03-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cnt2Transport.setRevisionsDescriptions(('Created.',))
if mibBuilder.loadTexts: cnt2Transport.setLastUpdated('0103090000Z')
if mibBuilder.loadTexts: cnt2Transport.setOrganization('Computer Network Technology Corporation')
if mibBuilder.loadTexts: cnt2Transport.setContactInfo('Computer Network Technology Technical Support 6000 Nathan Lane North Plymouth, Minnesota 55442 telephone: (763) 268-6000 fax: (763) 268-6800 support: 1-800-NET-TECH')
if mibBuilder.loadTexts: cnt2Transport.setDescription('This defines the CNT Transport MIB. The Transport layer provides network link for CNT proprietary traffic.')
cnt2TransportTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1), )
if mibBuilder.loadTexts: cnt2TransportTable.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportTable.setDescription('A list of Transport network link entries.')
cnt2TransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1), ).setIndexNames((0, "CNT246-MIB", "cnt2TransportSlotIndex"), (0, "CNT246-MIB", "cnt2TransportIndex"))
if mibBuilder.loadTexts: cnt2TransportEntry.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportEntry.setDescription('A Transport network link entry.')
cnt2TransportSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportSlotIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportSlotIndex.setDescription('The slot index for this Transport entry')
cnt2TransportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportIndex.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportIndex.setDescription('The relative index of the bus number in this Transport entry')
cnt2TransportBus = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportBus.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportBus.setDescription('The network link bus number')
cnt2TransportVid = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportVid.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportVid.setDescription('The virtual circuit number VCI. If ATM is used, make sure this Vid is configured the same as the VCI. Failure to do so will cause unexpected results')
cnt2TransportLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 9, 10, 11, 12, 13, 14, 99))).clone(namedValues=NamedValues(("atm", 8), ("ethernet", 9), ("fibrechannel", 10), ("fddi", 11), ("ds3e3", 12), ("lane", 13), ("ipv4", 14), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportLinkType.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportLinkType.setDescription('The Link type supported by the CNT Transport layer. ')
cnt2TransportLinkDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportLinkDesc.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportLinkDesc.setDescription('The description of the network link suported by the CNT Transport layer')
cnt2TransportLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportLinkStatus.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportLinkStatus.setDescription("The network link's status. The link status indicates if there is communication between the local node and the remote node. ")
cnt2TransportIPtosPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("routine", 1), ("priority", 2), ("immediate", 3), ("flash", 4), ("flashOverride", 5), ("criticECP", 6), ("internetworkControl", 7), ("networkControl", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportIPtosPrecedence.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportIPtosPrecedence.setDescription("The service precedence of IP Type of Service use by this link. There is an 8 bit field in an IP datagram that specifies the type of service a datagram is requesting (or hinting). It may then be used by the network to determine paths and precedence for a given datagram. The specific bits used may vary depending on the network (see RFC 791 for more details). The IpServiceType attribute can be used on a per circuit basis to specify the bits to be set in the IP datagram's service type field. Each Transport IP datagram destined for the DestionationIpAddress will have this field set. This attributes only applicable to IP providers. The service precedence is in bit 0-2 of the 8 bit IP Type of Service field.")
cnt2TransportIPtosDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("low", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportIPtosDelay.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportIPtosDelay.setDescription('The IP Type of Service Delay option use by this link. The Delay bit is in bit 3 of the 8 bit IP Type of Service field.')
cnt2TransportIPtosThruput = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportIPtosThruput.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportIPtosThruput.setDescription('The IP Type of Service Throughput option use by this link. The Throughput bit is in bit 4 of the 8 bit IP Type of Service field.')
cnt2TransportIPtosRelibility = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportIPtosRelibility.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportIPtosRelibility.setDescription('The IP Type of Service Relibility option use by this link. The Relibility bit is in bit 5 of the 8 bit IP Type of Service field.')
cnt2TransportRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportRemoteIp.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportRemoteIp.setDescription('The remote IP address. This address is set when Transport is configured.')
cnt2TransportProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("sap", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportProtocol.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportProtocol.setDescription('The protocol used by this link. At the moment the only protocol is SAP.')
cnt2TransportCompressionOption = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportCompressionOption.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportCompressionOption.setDescription('Reflects whether compression option is turned on/off.')
cnt2TransportMaxXmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportMaxXmitRate.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportMaxXmitRate.setDescription('The Maximum Transfer Rate of this link.')
cnt2TransportResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportResetTime.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportResetTime.setDescription('The time, in seconds, when the stats was last reset.')
cnt2TransportInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportInPkts.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportInPkts.setDescription('The number of packets transmitted to the link')
cnt2TransportInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportInOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportInOctets.setDescription('The number of bytes transmitted to the link ')
cnt2TransportOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportOutPkts.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportOutPkts.setDescription('The number of packets transmitted out from the link')
cnt2TransportOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportOutOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportOutOctets.setDescription('The number of bytes transmitted out from the link ')
cnt2TransportRexmit = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportRexmit.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportRexmit.setDescription('The number of packets being retransmitted')
cnt2TransportOosHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportOosHigh.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportOosHigh.setDescription('The number of out of sequence packets received')
cnt2TransportStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("all", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnt2TransportStatsReset.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportStatsReset.setDescription('Setting this will result the Transport statistic to be reset')
cnt2TransportRawOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportRawOutOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportRawOutOctets.setDescription('The number of bytes transmitted out from the lower interface of Transport layer. This is the amount of data after Compression plus Transport header. ')
cnt2TransportRawInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportRawInOctets.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportRawInOctets.setDescription('The number of bytes received in from the lower interface of Transport layer. This is the amount of data after Compression plus Transport header. ')
cnt2TransportWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportWindowSize.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportWindowSize.setDescription('The current window size, value is number buffers outstanding on the connection')
cnt2TransportSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportSegmentSize.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportSegmentSize.setDescription(' Range from (0 to 65532) If this value is non-zero, this value is used for segmentation. If equal to 0, then TransportSegmentSizeHi is what being used.')
cnt2TransportSegmentSizeHi = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportSegmentSizeHi.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportSegmentSizeHi.setDescription(" Range from (0 to 65532) If this value is used when TransportSegmentSize is set to 0. This value is passed in from user layer's MTU size.")
cnt2TransportRoundTripTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportRoundTripTimer.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportRoundTripTimer.setDescription('The current round trip timer. each count is in 50msec.')
cnt2TransportHoldCount = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportHoldCount.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportHoldCount.setDescription('The current hold count.')
cnt2TransportHoldCountRatio1 = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio1.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio1.setDescription('Incremented when an ack is received and there is no data on the hold queue and there is no outstanding (unacked) data. It indicates that transmission is idled until more data is received from the user.')
cnt2TransportHoldCountRatio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio2.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio2.setDescription('Incremented when an ack is received and there is no data on the hold queue but there is outstanding (unacked) data.')
cnt2TransportHoldCountRatio3 = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio3.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportHoldCountRatio3.setDescription('Incremented when an ack is received and there is data on the hold queue ready to be sent.')
cnt2TransportTotalDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 6, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2TransportTotalDisconnect.setStatus('current')
if mibBuilder.loadTexts: cnt2TransportTotalDisconnect.setDescription('Total disconnects at Transport Layer.')
mibBuilder.exportSymbols("CNT246-MIB", cnt2TransportTable=cnt2TransportTable, cnt2TransportRawOutOctets=cnt2TransportRawOutOctets, cnt2TransportOutOctets=cnt2TransportOutOctets, cnt2TransportSegmentSize=cnt2TransportSegmentSize, cnt2TransportLinkStatus=cnt2TransportLinkStatus, cnt2TransportResetTime=cnt2TransportResetTime, cnt2TransportMaxXmitRate=cnt2TransportMaxXmitRate, PYSNMP_MODULE_ID=cnt2Transport, cnt2TransportOutPkts=cnt2TransportOutPkts, cnt2TransportIPtosThruput=cnt2TransportIPtosThruput, cnt2TransportIndex=cnt2TransportIndex, cnt2TransportInOctets=cnt2TransportInOctets, cnt2TransportWindowSize=cnt2TransportWindowSize, cnt2TransportRoundTripTimer=cnt2TransportRoundTripTimer, cnt2TransportHoldCountRatio1=cnt2TransportHoldCountRatio1, cnt2TransportCompressionOption=cnt2TransportCompressionOption, cnt2TransportSegmentSizeHi=cnt2TransportSegmentSizeHi, cnt2TransportHoldCount=cnt2TransportHoldCount, cnt2TransportLinkType=cnt2TransportLinkType, cnt2TransportStatsReset=cnt2TransportStatsReset, cnt2TransportSlotIndex=cnt2TransportSlotIndex, cnt2TransportOosHigh=cnt2TransportOosHigh, cnt2TransportRemoteIp=cnt2TransportRemoteIp, cnt2TransportRawInOctets=cnt2TransportRawInOctets, cnt2TransportHoldCountRatio3=cnt2TransportHoldCountRatio3, cnt2TransportLinkDesc=cnt2TransportLinkDesc, cnt2TransportEntry=cnt2TransportEntry, cnt2TransportIPtosRelibility=cnt2TransportIPtosRelibility, cnt2TransportHoldCountRatio2=cnt2TransportHoldCountRatio2, cnt2TransportBus=cnt2TransportBus, cnt2TransportIPtosPrecedence=cnt2TransportIPtosPrecedence, cnt2Transport=cnt2Transport, cnt2TransportInPkts=cnt2TransportInPkts, cnt2TransportRexmit=cnt2TransportRexmit, cnt2TransportVid=cnt2TransportVid, cnt2TransportProtocol=cnt2TransportProtocol, cnt2TransportIPtosDelay=cnt2TransportIPtosDelay, cnt2TransportTotalDisconnect=cnt2TransportTotalDisconnect)