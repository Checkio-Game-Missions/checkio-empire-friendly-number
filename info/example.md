**Example:**

```python
friendly_number(102) == '102'
friendly_number(10240) == '10k'
friendly_number(12341234, decimals=1) == '12.3M'
friendly_number(12000000, decimals=3) == '12.000M'
friendly_number(12461, decimals=1) == '12.5k'
friendly_number(1024000000, base=1024, suffix='iB') == '976MiB'
friendly_number(-150, base=100, powers=['', 'd', 'D']) == '-1d'
friendly_number(-155, base=100, decimals=1, powers=['', 'd', 'D']) == '-1.6d'
friendly_number(255000000000, powers=['', 'k', 'M']) == '255000M'
```
