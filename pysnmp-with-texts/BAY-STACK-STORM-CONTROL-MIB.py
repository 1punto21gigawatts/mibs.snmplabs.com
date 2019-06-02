#
# PySNMP MIB module BAY-STACK-STORM-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-STORM-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, Integer32, iso, MibIdentifier, ModuleIdentity, IpAddress, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "Integer32", "iso", "MibIdentifier", "ModuleIdentity", "IpAddress", "NotificationType", "Counter64", "Bits")
TextualConvention, TimeInterval, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "DisplayString", "TruthValue")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackStormControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 42))
bayStackStormControlMib.setRevisions(('2014-03-04 00:00', '2012-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackStormControlMib.setRevisionsDescriptions(('Ver 2: Changed syntax for bsStormControlTrafficType.', 'Ver 1: Initial version.',))
if mibBuilder.loadTexts: bayStackStormControlMib.setLastUpdated('201403040000Z')
if mibBuilder.loadTexts: bayStackStormControlMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackStormControlMib.setContactInfo('avaya.com')
if mibBuilder.loadTexts: bayStackStormControlMib.setDescription('This MIB module is used for Storm Control configuration. The Storm Control feature prevents traffic on a LAN from being disrupted by a broadcast, multicast, or unicast storm on an interface.')
bsStormControlNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 42, 0))
bsStormControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 42, 1))
bsStormControlScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 1))
bsStormControlPollValue = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsStormControlPollValue.setStatus('current')
if mibBuilder.loadTexts: bsStormControlPollValue.setDescription('The polled value when a notification is generated.')
bsStormControlTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2), )
if mibBuilder.loadTexts: bsStormControlTable.setStatus('current')
if mibBuilder.loadTexts: bsStormControlTable.setDescription('This table is used to configure storm control global settings.')
bsStormControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"))
if mibBuilder.loadTexts: bsStormControlEntry.setStatus('current')
if mibBuilder.loadTexts: bsStormControlEntry.setDescription('An entry containing objects for controlling storm control settings.')
bsStormControlTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unicast", 1), ("broadcast", 2), ("multicast", 3))))
if mibBuilder.loadTexts: bsStormControlTrafficType.setStatus('current')
if mibBuilder.loadTexts: bsStormControlTrafficType.setDescription('Storm control traffic type.')
bsStormControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlEnabled.setStatus('current')
if mibBuilder.loadTexts: bsStormControlEnabled.setDescription('Indicates whether storm control is enabled for this instance.')
bsStormControlLowWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000000)).clone(200)).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlLowWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlLowWatermark.setDescription('Low watermark for storm control of this instance. If the rate drops below this value after having risen above the high watermark, a single notification will be generated.')
bsStormControlHighWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000000)).clone(500)).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlHighWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlHighWatermark.setDescription('High watermark for storm control of this instance. If the rate rises above this value, notifications will be generated at the rate give by the bsStormControlTrapInterval object.')
bsStormControlPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 5), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(500, 30000)).clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlPollInterval.setStatus('current')
if mibBuilder.loadTexts: bsStormControlPollInterval.setDescription('The polling interval for checking the packet rate for storm control of this instance.')
bsStormControlTrapInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlTrapInterval.setStatus('current')
if mibBuilder.loadTexts: bsStormControlTrapInterval.setDescription('The rate for sending storm control notifications, measured in a number of polling intervals.')
bsStormControlActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("drop", 2), ("shutdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlActionType.setStatus('current')
if mibBuilder.loadTexts: bsStormControlActionType.setDescription('Storm control action type for this instance.')
bsStormControlIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3), )
if mibBuilder.loadTexts: bsStormControlIfTable.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfTable.setDescription('This table is used to control storm control settings per-interface.')
bsStormControlIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"), (0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlIfIndex"))
if mibBuilder.loadTexts: bsStormControlIfEntry.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfEntry.setDescription('An entry containing objects for controlling storm control settings for an interface.')
bsStormControlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsStormControlIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfIndex.setDescription('The ifIndex value of the interface.')
bsStormControlIfEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfEnabled.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfEnabled.setDescription('Indicates whether storm control is enabled for this instance.')
bsStormControlIfLowWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000000)).clone(200)).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfLowWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfLowWatermark.setDescription('Low watermark for storm control of this instance. If the rate drops below this value after having risen above the high watermark, a single notification will be generated.')
bsStormControlIfHighWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000000)).clone(500)).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfHighWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfHighWatermark.setDescription('High watermark for storm control of this instance. If the rate rises above this value, notifications will be generated at the rate give by the bsStormControlTrapInterval object.')
bsStormControlIfPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 5), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(500, 30000)).clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfPollInterval.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfPollInterval.setDescription('The polling interval for checking the packet rate for storm control of this instance.')
bsStormControlIfTrapInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfTrapInterval.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfTrapInterval.setDescription('The rate for sending storm control notifications.')
bsStormControlIfActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("drop", 2), ("shutdown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsStormControlIfActionType.setStatus('current')
if mibBuilder.loadTexts: bsStormControlIfActionType.setDescription('Storm control action type for this instance.')
bsStormControlBelowLowWatermark = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 42, 0, 1)).setObjects(("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"), ("IF-MIB", "ifIndex"), ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlPollValue"), ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlLowWatermark"))
if mibBuilder.loadTexts: bsStormControlBelowLowWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlBelowLowWatermark.setDescription('This notification is generated when the storm control packet type rate falls below the low watermark after having risen above the high watermark. It is generated only once when this occurs.')
bsStormControlAboveHighWatermark = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 42, 0, 2)).setObjects(("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"), ("IF-MIB", "ifIndex"), ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlPollValue"), ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlHighWatermark"))
if mibBuilder.loadTexts: bsStormControlAboveHighWatermark.setStatus('current')
if mibBuilder.loadTexts: bsStormControlAboveHighWatermark.setDescription('This notification is generated periodically as long as the storm control packet type rate remains above the high watermark.')
mibBuilder.exportSymbols("BAY-STACK-STORM-CONTROL-MIB", bsStormControlActionType=bsStormControlActionType, bsStormControlAboveHighWatermark=bsStormControlAboveHighWatermark, bsStormControlPollInterval=bsStormControlPollInterval, bsStormControlHighWatermark=bsStormControlHighWatermark, PYSNMP_MODULE_ID=bayStackStormControlMib, bsStormControlTrafficType=bsStormControlTrafficType, bsStormControlIfEnabled=bsStormControlIfEnabled, bsStormControlObjects=bsStormControlObjects, bsStormControlEnabled=bsStormControlEnabled, bsStormControlTable=bsStormControlTable, bsStormControlIfIndex=bsStormControlIfIndex, bsStormControlIfEntry=bsStormControlIfEntry, bsStormControlIfLowWatermark=bsStormControlIfLowWatermark, bsStormControlTrapInterval=bsStormControlTrapInterval, bsStormControlIfTrapInterval=bsStormControlIfTrapInterval, bsStormControlBelowLowWatermark=bsStormControlBelowLowWatermark, bsStormControlLowWatermark=bsStormControlLowWatermark, bsStormControlIfActionType=bsStormControlIfActionType, bsStormControlIfPollInterval=bsStormControlIfPollInterval, bsStormControlIfTable=bsStormControlIfTable, bayStackStormControlMib=bayStackStormControlMib, bsStormControlScalars=bsStormControlScalars, bsStormControlIfHighWatermark=bsStormControlIfHighWatermark, bsStormControlEntry=bsStormControlEntry, bsStormControlPollValue=bsStormControlPollValue, bsStormControlNotifications=bsStormControlNotifications)