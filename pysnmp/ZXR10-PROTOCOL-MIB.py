#
# PySNMP MIB module ZXR10-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, ObjectIdentity, Integer32, iso, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, Gauge32, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "Gauge32", "MibIdentifier", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10protocol = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101))
zxr10ip = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1))
zxr10tcp = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2))
class DisplayString(OctetString):
    pass

zxr10ipvrfaddrTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1), )
if mibBuilder.loadTexts: zxr10ipvrfaddrTable.setStatus('current')
zxr10ipvrfaddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1), ).setIndexNames((0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfVpnName"), (0, "ZXR10-PROTOCOL-MIB", "zxr10ipVrfAddr"))
if mibBuilder.loadTexts: zxr10ipvrfaddrEntry.setStatus('current')
zxr10ipVrfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfVpnName.setStatus('current')
zxr10ipVrfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfAddr.setStatus('current')
zxr10ipVrfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfNetMask.setStatus('current')
zxr10ipVrfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfIfIndex.setStatus('current')
zxr10ipVrfBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfBcastAddr.setStatus('current')
zxr10ipVrfReasmMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10ipVrfReasmMaxSize.setStatus('current')
zxr10tcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1), )
if mibBuilder.loadTexts: zxr10tcpConnTable.setStatus('current')
zxr10tcpconnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1), ).setIndexNames((0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnVrfVpnName"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalAddress"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnLocalPort"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemAddress"), (0, "ZXR10-PROTOCOL-MIB", "zxr10tcpConnRemPort"))
if mibBuilder.loadTexts: zxr10tcpconnEntry.setStatus('current')
zxr10tcpConnVrfVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnVrfVpnName.setStatus('current')
zxr10tcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10tcpConnState.setStatus('current')
zxr10tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnLocalAddress.setStatus('current')
zxr10tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnLocalPort.setStatus('current')
zxr10tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnRemAddress.setStatus('current')
zxr10tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10tcpConnRemPort.setStatus('current')
mibBuilder.exportSymbols("ZXR10-PROTOCOL-MIB", zxr10tcpConnLocalAddress=zxr10tcpConnLocalAddress, zxr10=zxr10, zxr10tcpConnRemAddress=zxr10tcpConnRemAddress, zte=zte, zxr10ipVrfNetMask=zxr10ipVrfNetMask, zxr10tcpConnRemPort=zxr10tcpConnRemPort, zxr10protocol=zxr10protocol, zxr10ip=zxr10ip, zxr10ipVrfIfIndex=zxr10ipVrfIfIndex, zxr10tcpConnState=zxr10tcpConnState, zxr10tcpConnVrfVpnName=zxr10tcpConnVrfVpnName, zxr10ipVrfReasmMaxSize=zxr10ipVrfReasmMaxSize, zxr10tcpConnLocalPort=zxr10tcpConnLocalPort, zxr10ipvrfaddrEntry=zxr10ipvrfaddrEntry, DisplayString=DisplayString, zxr10ipVrfVpnName=zxr10ipVrfVpnName, zxr10ipvrfaddrTable=zxr10ipvrfaddrTable, zxr10tcpconnEntry=zxr10tcpconnEntry, zxr10tcpConnTable=zxr10tcpConnTable, zxr10tcp=zxr10tcp, zxr10ipVrfBcastAddr=zxr10ipVrfBcastAddr, zxr10ipVrfAddr=zxr10ipVrfAddr)