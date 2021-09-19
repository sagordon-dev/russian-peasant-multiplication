# Russian Peasant Multiplication

## RPM by Hand

### Problem Statement

Multiply 89 by 18

#### RPM Chart for 89 X 18

|Halving|Doubling|
|:-------|:-------|
|89     |18     |
|     |       |
|     |       |
|     |       |
|      |       |
|      |       |
|      |       |

|Halving|Doubling|
|:-------|:-------|
|89     |18     |
|44     |       |
|22     |       |
|11     |       |
|5      |       |
|2      |       |
|1      |       |
**Halve values in the halving column until 1**

|Halving|Doubling|
|:-------|:-------|
|89     |18     |
|44     |36     |
|22     |72     |
|11     |144    |
|5      |288    |
|2      |576    |
|1      |1,152  |
**Double values in the doubling column**

|Halving|Doubling|
|:-------|:-------|
|89     |18     |
|~~44~~ |~~36~~ |
|~~22~~ |~~72~~ |
|11     |144    |
|5      |288    |
|~~2~~  |~~576~~|
|1      |1,152  |
**Remove rows where the halving column has an even number.**

|Halving|Doubling|
|:-------|:-------|
|89     |18     |
|11     |144    |
|5      |288    |
|1      |1,152  |
**Take the sum of the remaining entries in the doubling column**

$18 - 144 + 288 +1,152 = 1,602$

$89 \times 18 = 1,602$
