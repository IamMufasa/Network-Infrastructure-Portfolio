# Wireless Network Planning Document
# UF Campus Building Wireless Deployment

## Executive Summary

This document outlines the wireless network planning for a new academic building at the University of Florida campus. The deployment follows UF IT's telecommunications standards and best practices for wireless coverage, capacity, and performance.

## Building Specifications

- Building Name: New Science Building
- Total Area: 45,000 sq ft
- Floors: 3
- Primary Usage: Classrooms, Labs, Faculty Offices
- Expected Occupancy: 800-1000 users
- Construction Type: Concrete and steel with drywall partitions

## Wireless Requirements

- Coverage: 100% of usable space
- Minimum Signal Strength: -65 dBm
- Minimum SNR: 25 dB
- Supported Standards: 802.11a/b/g/n/ac/ax (WiFi 6)
- Authentication: 802.1X with WPA2-Enterprise
- SSIDs:
  - UF (Faculty/Staff)
  - UF Guest (Visitors)
  - eduroam (Academic roaming)

## Access Point Planning

### Access Point Model Selection

Selected AP Model: Cisco Catalyst 9130AX Series
Justification:
- WiFi 6 (802.11ax) support for high-density environments
- Dual 5 GHz radios for increased capacity
- Compatibility with existing UF wireless infrastructure
- Advanced security features
- Integrated BLE for location services

### Access Point Placement Strategy

#### Floor 1 (15,000 sq ft)
- Total APs: 12
- Placement Strategy: Grid pattern with 30-35 ft spacing
- Special Considerations: 
  - Higher density in lecture halls and common areas
  - Outdoor coverage for entrance areas

#### Floor 2 (15,000 sq ft)
- Total APs: 14
- Placement Strategy: Grid pattern with 30-35 ft spacing
- Special Considerations:
  - Higher density in laboratory spaces
  - Coverage for meeting rooms and collaboration spaces

#### Floor 3 (15,000 sq ft)
- Total APs: 10
- Placement Strategy: Grid pattern with 30-35 ft spacing
- Special Considerations:
  - Faculty offices with lower density requirements
  - Coverage for research spaces

### Channel Planning

#### 2.4 GHz Band
- Available Channels: 1, 6, 11
- Channel Width: 20 MHz
- Channel Reuse Pattern: 3-cell pattern to minimize co-channel interference

#### 5 GHz Band
- Available Channels: 36-64, 100-144
- Channel Width: 40 MHz (primary), 80 MHz (where possible)
- DFS Channels: Enabled where regulatory compliance permits
- Channel Reuse Pattern: Designed to minimize adjacent and co-channel interference

## Wireless Survey Methodology

### Pre-deployment Survey
- Tool: Ekahau Pro
- Survey Type: Predictive and Active
- Measurement Points: Minimum 1 per 500 sq ft
- Metrics Collected:
  - Signal strength (RSSI)
  - Signal-to-noise ratio (SNR)
  - Co-channel interference
  - Coverage overlap

### Post-deployment Validation
- Tool: Ekahau Pro
- Survey Type: Active
- Measurement Points: Minimum 1 per 500 sq ft
- Validation Criteria:
  - Signal strength ≥ -65 dBm in 95% of coverage area
  - SNR ≥ 25 dB in 95% of coverage area
  - Successful roaming between APs
  - Throughput testing (minimum 100 Mbps)

## Wireless Controller Configuration

### Controller Model
- Cisco Catalyst 9800 Series Wireless Controller

### AP Groups and RF Profiles
- AP Group: NSB-APGroup
- RF Profiles:
  - NSB-HighDensity (lecture halls, common areas)
  - NSB-Standard (offices, corridors)
  - NSB-Outdoor (entrance areas)

### QoS Configuration
- Voice: Priority queuing, DSCP 46
- Video: Priority queuing, DSCP 34
- Best Effort: Default for most traffic
- Background: Lowest priority

## Implementation Timeline

1. Pre-deployment Survey: Week 1
2. AP Mounting and Cabling: Weeks 2-3
3. Controller Configuration: Week 3
4. AP Installation and Initial Configuration: Week 4
5. Post-deployment Validation: Week 5
6. Optimization and Tuning: Week 6
7. Documentation and Handover: Week 7

## Budget Estimate

- Hardware (36 APs @ $1,200 each): $43,200
- Cabling and Mounting: $18,000
- Survey and Implementation Services: $25,000
- Documentation and Training: $5,000
- Total Estimated Cost: $91,200

## Conclusion

This wireless network plan provides comprehensive coverage and capacity for the New Science Building, meeting all UF IT telecommunications standards and best practices. The implementation follows industry standards for high-density academic environments and provides a robust foundation for future expansion and technology upgrades.
