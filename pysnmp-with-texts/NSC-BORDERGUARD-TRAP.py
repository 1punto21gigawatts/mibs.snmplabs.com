#
# PySNMP MIB module NSC-BORDERGUARD-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSC-BORDERGUARD-TRAP
# Produced by pysmi-0.3.4 at Wed May  1 14:24:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nscBorderGuard, = mibBuilder.importSymbols("NSC-MIB", "nscBorderGuard")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Counter32, Counter64, iso, TimeTicks, IpAddress, Gauge32, ModuleIdentity, Unsigned32, Integer32, NotificationType, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter32", "Counter64", "iso", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nscBorderGuardTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1))
nscBorderGuardTrapsBadImage = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsBadImage.setStatus('mandatory')
if mibBuilder.loadTexts: nscBorderGuardTrapsBadImage.setDescription('This represents the image with bad CRC.')
nscBorderGuardTrapsCurrentImage = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 2), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsCurrentImage.setStatus('mandatory')
if mibBuilder.loadTexts: nscBorderGuardTrapsCurrentImage.setDescription('This represents the image currently running in the system.')
nscBorderGuardTrapsBadFileSystem = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 3), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsBadFileSystem.setStatus('mandatory')
if mibBuilder.loadTexts: nscBorderGuardTrapsBadFileSystem.setDescription('This represents the file system with an erased condition.')
nscBorderGuardTrapsSoftFault = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 4), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsSoftFault.setStatus('mandatory')
if mibBuilder.loadTexts: nscBorderGuardTrapsSoftFault.setDescription('This represents the code for a Soft Fault.')
nscBorderGuardTrapsEventReason = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: nscBorderGuardTrapsEventReason.setStatus('mandatory')
if mibBuilder.loadTexts: nscBorderGuardTrapsEventReason.setDescription('This represents the reason (in ASCII text) of a BorderGuarder Access Router event.')
nscBorderGuardBadCRC = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,1)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadImage"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsCurrentImage"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
if mibBuilder.loadTexts: nscBorderGuardBadCRC.setDescription('This trap indicates that a corrupted image occured.')
nscBorderGuardBadFileSystem = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,2)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadFileSystem"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
if mibBuilder.loadTexts: nscBorderGuardBadFileSystem.setDescription('This trap indicates that a file system was erased.')
nscBorderGuardSoftFault = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,3)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsSoftFault"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
if mibBuilder.loadTexts: nscBorderGuardSoftFault.setDescription('This trap indicates that a soft fault occured.')
mibBuilder.exportSymbols("NSC-BORDERGUARD-TRAP", nscBorderGuardTrapsSoftFault=nscBorderGuardTrapsSoftFault, nscBorderGuardBadCRC=nscBorderGuardBadCRC, nscBorderGuardSoftFault=nscBorderGuardSoftFault, nscBorderGuardTrapsBadImage=nscBorderGuardTrapsBadImage, nscBorderGuardTraps=nscBorderGuardTraps, nscBorderGuardBadFileSystem=nscBorderGuardBadFileSystem, nscBorderGuardTrapsEventReason=nscBorderGuardTrapsEventReason, nscBorderGuardTrapsBadFileSystem=nscBorderGuardTrapsBadFileSystem, nscBorderGuardTrapsCurrentImage=nscBorderGuardTrapsCurrentImage)