#
# PySNMP MIB module HDSL700G3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HDSL700G3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hdsl700G3, = mibBuilder.importSymbols("GDCHDSL-MIB", "hdsl700G3")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Unsigned32, Bits, iso, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Gauge32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "iso", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Gauge32", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hdsl700G3System = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 1))
hdsl700G3Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 1, 1))
gdc700G3SystemMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 11, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gdc700G3SystemMIBversion.setStatus('mandatory')
hdsl700G3Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2))
hdsl700G3NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 1))
hdsl700G3DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 2))
hdsl700G3PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 3))
hdsl700G3UnitFailure = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 4))
hdsl700G3ChecksumCorrupt = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 5))
hdsl700G3LossofSignal = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 6))
hdsl700G3UnavailableSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 7))
hdsl700G3ErrorSec = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 8))
hdsl700G3LossofSyncWord = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 9))
hdsl700G3LossofFrameAlign = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 10))
hdsl700G3AllOnes = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 11))
hdsl700G3RemoteLossofSig = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 12))
hdsl700G3RemoteAlarmInd = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 13))
hdsl700G3MajorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 14))
hdsl700G3MinorBER = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 11, 3, 2, 15))
mibBuilder.exportSymbols("HDSL700G3-MIB", hdsl700G3ErrorSec=hdsl700G3ErrorSec, hdsl700G3PowerUpAlm=hdsl700G3PowerUpAlm, hdsl700G3System=hdsl700G3System, hdsl700G3NoResponseAlm=hdsl700G3NoResponseAlm, hdsl700G3LossofFrameAlign=hdsl700G3LossofFrameAlign, gdc700G3SystemMIBversion=gdc700G3SystemMIBversion, hdsl700G3AllOnes=hdsl700G3AllOnes, hdsl700G3LossofSignal=hdsl700G3LossofSignal, hdsl700G3MajorBER=hdsl700G3MajorBER, hdsl700G3ChecksumCorrupt=hdsl700G3ChecksumCorrupt, hdsl700G3RemoteAlarmInd=hdsl700G3RemoteAlarmInd, hdsl700G3LossofSyncWord=hdsl700G3LossofSyncWord, hdsl700G3Alarms=hdsl700G3Alarms, hdsl700G3MinorBER=hdsl700G3MinorBER, hdsl700G3UnavailableSec=hdsl700G3UnavailableSec, hdsl700G3DiagRxErrAlm=hdsl700G3DiagRxErrAlm, hdsl700G3UnitFailure=hdsl700G3UnitFailure, hdsl700G3RemoteLossofSig=hdsl700G3RemoteLossofSig, hdsl700G3Version=hdsl700G3Version)