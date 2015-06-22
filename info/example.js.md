**Example:**

```javascript
friendlyNumber(102) == '102'
friendlyNumber(10240) == '10k'
friendlyNumber(12341234, {decimals: 1}) == '12.3M'
friendlyNumber(12000000, {decimals: 3}) == '12.000M'
friendlyNumber(12461, {decimals: 1}) == '12.5k'
friendlyNumber(1024000000, {base: 1024, suffix: 'iB'}) == '976MiB'
friendlyNumber(-150, {base: 100, powers: ['', 'd', 'D']}) == '-1d'
friendlyNumber(-155, {base: 100, decimals:1, powers: ['', 'd', 'D']}) == '-1.6d'
friendlyNumber(255000000000, {powers: ['', 'k', 'M']}) == '255000M'
```
