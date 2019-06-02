#
# PySNMP MIB module TOW-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOW-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, Unsigned32, NotificationType, ModuleIdentity, Integer32, IpAddress, enterprises, Counter64, iso, Gauge32, ObjectIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Unsigned32", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "enterprises", "Counter64", "iso", "Gauge32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
class DisplayString(OctetString):
    pass

cdx6500TOWCfgTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22), )
if mibBuilder.loadTexts: cdx6500TOWCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TOWCfgTable.setDescription('This table contains the configuration parameters for TOW.')
cdx6500TOWCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1), ).setIndexNames((0, "TOW-OPT-MIB", "cdx6500TowCfgEntryNum"))
if mibBuilder.loadTexts: cdx6500TOWCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TOWCfgEntry.setDescription('Configuration parameters for each TOW entry.')
cdx6500TowCfgEntryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgEntryNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgEntryNum.setDescription('Entry number used to reference this table record.')
cdx6500TowCfgEntryName = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgEntryName.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgEntryName.setDescription('Range = 0-20 alphanumeric characters, use the space character to blank field.')
cdx6500TowCfgInt1StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt1StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt1StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt1Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt1Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt1Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt1StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt1StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt1StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt2StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt2StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt2StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt2Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt2Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt2Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt2StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt2StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt2StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt3StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt3StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt3StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt3Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt3Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt3Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt3StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt3StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt3StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt4StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt4StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt4StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt4Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt4Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt4Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt4StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt4StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt4StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt5StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt5StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt5StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt5Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt5Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt5Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt5StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt5StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt5StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt6StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt6StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt6StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt6Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt6Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt6Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt6StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt6StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt6StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt7StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt7StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt7StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt7Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt7Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt7Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt7StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt7StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt7StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt8StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt8StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt8StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt8Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt8Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt8Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt8StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt8StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt8StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt9StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt9StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt9StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt9Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt9Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt9Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt9StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt9StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt9StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
cdx6500TowCfgInt10StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt10StartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt10StartTime.setDescription('This parameter specifies the start time of the interval. Format : hh:mm hh : Is the start hour , with range 00 to 23. mm : Is the start minute, with range 00 to 59. This parameter specifies the start time of the interval. All the intervals configured in an entry do not overlap. Intervals configured in different entries can overlap.')
cdx6500TowCfgInt10Duration = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 31), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt10Duration.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt10Duration.setDescription('Format : dd:hh:mm dd : Days . Range 00 to 06. hh : Hours. Range 00 to 23. mm : minutes. Range 00 to 59. This parameter specifies the duration of the interval starting from the start time configured. To check if the end time of the interval is as desired, check the Time of Week intervals under the statistics menu.')
cdx6500TowCfgInt10StartDays = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 27))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TowCfgInt10StartDays.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500TowCfgInt10StartDays.setDescription("DDD : This specifies the day. Range is one of MON TUE WED THU FRI SAT SUN. DDD+DDD+DDD : This specifies that the interval has to start on each of these days. The `+' operator implies AND. A maximum of 7 days can be specified. This parameter specifies the days on which the interval has to be applied. That is, the intervals would start on each of these days.")
mibBuilder.exportSymbols("TOW-OPT-MIB", cdx6500TowCfgInt1Duration=cdx6500TowCfgInt1Duration, cdx6500TowCfgInt2StartTime=cdx6500TowCfgInt2StartTime, cdx6500TowCfgInt5StartDays=cdx6500TowCfgInt5StartDays, cdx6500TowCfgInt3Duration=cdx6500TowCfgInt3Duration, cdx6500TowCfgInt9Duration=cdx6500TowCfgInt9Duration, cdx6500TowCfgInt6StartTime=cdx6500TowCfgInt6StartTime, cdx6500TowCfgInt7Duration=cdx6500TowCfgInt7Duration, cdx6500TowCfgInt7StartDays=cdx6500TowCfgInt7StartDays, cdxProductSpecific=cdxProductSpecific, cdx6500TowCfgInt7StartTime=cdx6500TowCfgInt7StartTime, cdx6500TOWCfgTable=cdx6500TOWCfgTable, cdx6500TowCfgInt6Duration=cdx6500TowCfgInt6Duration, cdx6500TowCfgInt9StartDays=cdx6500TowCfgInt9StartDays, cdx6500TowCfgInt8Duration=cdx6500TowCfgInt8Duration, cdx6500TowCfgInt5Duration=cdx6500TowCfgInt5Duration, cdx6500TowCfgInt5StartTime=cdx6500TowCfgInt5StartTime, cdx6500TowCfgInt2Duration=cdx6500TowCfgInt2Duration, cdx6500TowCfgInt4StartTime=cdx6500TowCfgInt4StartTime, cdx6500TowCfgInt3StartTime=cdx6500TowCfgInt3StartTime, cdx6500TowCfgInt4Duration=cdx6500TowCfgInt4Duration, cdx6500TowCfgInt10Duration=cdx6500TowCfgInt10Duration, cdx6500TowCfgInt6StartDays=cdx6500TowCfgInt6StartDays, DisplayString=DisplayString, cdx6500TowCfgEntryNum=cdx6500TowCfgEntryNum, cdx6500TowCfgInt4StartDays=cdx6500TowCfgInt4StartDays, cdx6500TowCfgInt10StartTime=cdx6500TowCfgInt10StartTime, cdx6500TowCfgInt1StartDays=cdx6500TowCfgInt1StartDays, cdx6500TowCfgInt10StartDays=cdx6500TowCfgInt10StartDays, cdx6500Configuration=cdx6500Configuration, cdx6500TowCfgInt2StartDays=cdx6500TowCfgInt2StartDays, cdx6500TowCfgInt3StartDays=cdx6500TowCfgInt3StartDays, cdx6500=cdx6500, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, codex=codex, cdx6500TowCfgEntryName=cdx6500TowCfgEntryName, cdx6500TowCfgInt1StartTime=cdx6500TowCfgInt1StartTime, cdx6500TowCfgInt8StartDays=cdx6500TowCfgInt8StartDays, cdx6500TowCfgInt9StartTime=cdx6500TowCfgInt9StartTime, cdx6500TOWCfgEntry=cdx6500TOWCfgEntry, cdx6500TowCfgInt8StartTime=cdx6500TowCfgInt8StartTime)