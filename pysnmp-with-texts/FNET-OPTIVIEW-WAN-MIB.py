#
# PySNMP MIB module FNET-OPTIVIEW-WAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FNET-OPTIVIEW-WAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
fnetOptiViewGeneric, = mibBuilder.importSymbols("FNET-GLOBAL-REG", "fnetOptiViewGeneric")
ovTrapStatus, ovTrapSeverity, ovTrapAgentSysName, ovTrapDescription, ovTrapOffenderNetAddr, ovTrapOffenderName, ovTrapOffenderSubId = mibBuilder.importSymbols("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus", "ovTrapSeverity", "ovTrapAgentSysName", "ovTrapDescription", "ovTrapOffenderNetAddr", "ovTrapOffenderName", "ovTrapOffenderSubId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, iso, NotificationType, ModuleIdentity, ObjectIdentity, MibIdentifier, Gauge32, Counter64, TimeTicks, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64", "TimeTicks", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
probSonetLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12000)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probSonetLinkDown.setDescription('Monitor the contiguous Line Unavailable or Path Unavailable seconds on the Sonet link. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probSonetErrors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12001)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probSonetErrors.setDescription('Monitor the count of contiguous Sonet Line Errored seconds or Severely Errored seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probSonetAlarms = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12002)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probSonetAlarms.setDescription('Monitor the presence of Sonet alarms. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probAtmLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12003)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probAtmLinkDown.setDescription('Monitor the contiguous Loss of Cell Delineation seconds on the ATM link. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probAtmErrors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12004)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probAtmErrors.setDescription('Monitor the rate of the combination of correctable and uncorrectable HEC errors. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probPDUCRCErrors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12005)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probPDUCRCErrors.setDescription('Monitor the rate of PDU CRC errors. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probPosLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12006)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probPosLinkDown.setDescription('Monitor the contiguous loss of HDLC framing (LOF) seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probPosErrorsDetected = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12007)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probPosErrorsDetected.setDescription('Monitor the percentage of bad HDLC frames on the Pos link. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probLinkUtilization = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12008)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probLinkUtilization.setDescription('Monitor the utilization of the entire pipe bandwidth. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDNSServerNoResp = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12009)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDNSServerNoResp.setDescription('Monitor the status of the DNS server. When the management port receives no DNS reply from the server address configured via DHCP, and no DNS reply from either the primary or secondary servers statically configured by the user, and there was no reply to a broadcast message for a local DNS server, a trap is generated with ovTrapStatus=discovered. When the user causes a DNS server to be rediscovered via DHCP, or configures a valid primary or secondary servier statically, a trap is generated with ovTrapStatus=resolved.')
probDNSServerNowUsing = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12010)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDNSServerNowUsing.setDescription('Monitor the status of the DNS server. When the management port receives no DNS reply from the server address configured via DHCP, and no DNS reply from either the primary or secondary servers statically configured by the user, and there WAS a reply to a broadcast message for a local DNS server, a trap is generated with ovTrapStatus=discovered. When the user causes a DNS server to be rediscovered via DHCP, or statically configures a valid primary or secondary server, a trap is generated with ovTrapStatus=resolved.')
probLostDHCPLease = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12011)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probLostDHCPLease.setDescription("Monitor the status of the management port's DHCP lease. When the lease expires a single trap is generated with ovTrapStatus=discovered. When the default router resumes responding to the PING then a single trap is generated with ovTrapStatus=resolved.")
probDefaultRouterNoResp = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12012)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDefaultRouterNoResp.setDescription('Monitor PING responses from the default router. When no response is received the proble generates a single trap with ovTrapStatus=discovered. When the default router resumes responding to the PING then a single trap is generated with ovTrapStatus=resolved.')
probDiscoveryFull = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12013)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDiscoveryFull.setDescription('When the discovery databases are full a single trap is generated with ovTrapStatus=discovered. This indicates new hosts and virtual circuits.will not be added to the discovery database. RMON hosts, conversations, and utilization history will continue to be measured. Perform a rerun test when desired to clear the discovery database.')
probClearCounts = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12014)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probClearCounts.setDescription('When the user clears statistics for a specific measurement, a single trap is generated with ovTrapStatus=discovered, and ovTrapSeverity = inform. The type of statistic (e.g top VC) is indicated in the ovTrapDescription field.')
probDS1LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12015)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS1LinkDown.setDescription('Monitor the T1/E1 Errors and Alarms. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDS1Errors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12016)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS1Errors.setDescription('Monitor the count of contiguous T1/E1 Errored seconds or Severely Errored seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDS1Alarms = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12017)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS1Alarms.setDescription('Monitor the presence of T1/E1 alarms. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDS3LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12018)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS3LinkDown.setDescription('Monitor the DS1/E3 Errors and Alarms. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDS3Errors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12019)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS3Errors.setDescription('Monitor the count of contiguous DS3/E3 Errored seconds or Severely Errored seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probDS3Alarms = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12020)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probDS3Alarms.setDescription('Monitor the presence of DS1/E3 alarms. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probFrLmiLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12021)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probFrLmiLinkDown.setDescription('Monitor the contiguous inactive LMI seconds on the Frame Relay link. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probFrLmiErrors = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12022)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probFrLmiErrors.setDescription('Monitor LMI errors on the Frame Relay link. When the LMI errors exist, the Analyzer generates this trap with ovTrapStatus=discovered. When the LMI errors subside, the Analyzer generates this trap with ovTrapStatus=resolved.')
probFrErrorsDetected = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12023)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probFrErrorsDetected.setDescription('Monitor the count of contiguous Errored Frame seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probVcDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12024)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probVcDown.setDescription("Monitor the state of Frame Relay VCs. When the PVC status received via the local in-channel signaling reports status = 'deleted' or 'inactive', the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the in-channel signaling reports status = 'active' the Analyzer generates this trap with ovTrapStatus=resolved.")
probInvalidDlci = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12025)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probInvalidDlci.setDescription('Monitor the state of Frame Relay DLCI for invalid. When the Analyzer receives an inactive or unknown DLCI it generates this trap with ovTrapStatus=discovered. If the full-status LMI later reports the DLCI active, the Analyzer generates this trap with ovTrapStatus=resolved.')
probFrDEUnderCIRUtilization = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12026)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probFrDEUnderCIRUtilization.setDescription('Monitor the utilization of % DE under CIR. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probHdlcLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12027)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probHdlcLinkDown.setDescription('Monitor the contiguous loss of HDLC framing seconds. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probHdlcErrorsDetected = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12028)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probHdlcErrorsDetected.setDescription('Monitor the percentage of bad HDLC frames. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
probFrDteDceReversed = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12029)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probFrDteDceReversed.setDescription('WAN cable reversed from LMI discovered DTE/DCR (FR only).')
probKeyDevPingLatency = NotificationType((1, 3, 6, 1, 4, 1, 1226, 2, 1) + (0,12030)).setObjects(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"), ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderSubId"))
if mibBuilder.loadTexts: probKeyDevPingLatency.setDescription('Measures the roundtrip PING latency to a key device. When the count equals or exceeds the rising threshold, the Analyzer generates this trap with ovTrapStatus=discovered. Then, when the count descends back below the falling threshold the Analyzer generates this trap with ovTrapStatus=resolved.')
mibBuilder.exportSymbols("FNET-OPTIVIEW-WAN-MIB", probPosErrorsDetected=probPosErrorsDetected, probHdlcLinkDown=probHdlcLinkDown, probSonetAlarms=probSonetAlarms, probLinkUtilization=probLinkUtilization, probKeyDevPingLatency=probKeyDevPingLatency, probFrLmiErrors=probFrLmiErrors, probSonetErrors=probSonetErrors, probDS1Errors=probDS1Errors, probPosLinkDown=probPosLinkDown, probInvalidDlci=probInvalidDlci, probVcDown=probVcDown, probHdlcErrorsDetected=probHdlcErrorsDetected, probDiscoveryFull=probDiscoveryFull, probAtmErrors=probAtmErrors, probDS3Errors=probDS3Errors, probDNSServerNowUsing=probDNSServerNowUsing, probFrDEUnderCIRUtilization=probFrDEUnderCIRUtilization, probDS1Alarms=probDS1Alarms, probClearCounts=probClearCounts, probFrLmiLinkDown=probFrLmiLinkDown, probLostDHCPLease=probLostDHCPLease, probPDUCRCErrors=probPDUCRCErrors, probAtmLinkDown=probAtmLinkDown, probDS3LinkDown=probDS3LinkDown, probDNSServerNoResp=probDNSServerNoResp, probSonetLinkDown=probSonetLinkDown, probDS3Alarms=probDS3Alarms, probFrDteDceReversed=probFrDteDceReversed, probFrErrorsDetected=probFrErrorsDetected, probDS1LinkDown=probDS1LinkDown, probDefaultRouterNoResp=probDefaultRouterNoResp)