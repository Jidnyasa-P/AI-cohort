# Structured SQL Queries

## 1. Deductible on Gold PPO plan

**Question:** What is the deductible on the Gold PPO plan?

```sql
SELECT annual_deductible
FROM plans
WHERE plan_name = 'Gold PPO';
```

**Output:**
```text
(2000,)
```

## 2. Pending claims for member M1001

**Question:** How many claims are pending for member M1001?

```sql
SELECT COUNT(*) AS pending_claim_count
FROM claims
WHERE member_id = 'M1001' AND status = 'Pending';
```

**Output:**
```text
(1,)
```

## 3. Plans with monthly premium under $400

**Question:** Which plans have a monthly premium under $400?

```sql
SELECT plan_id, plan_name, monthly_premium
FROM plans
WHERE monthly_premium < 400
ORDER BY monthly_premium;
```

**Output:**
```text
('P103', 'Bronze HMO', 150)
('P102', 'Silver HMO', 300)
```

## 4. Join between claims and plans

**Question:** Show claims joined with the plan details.

```sql
SELECT c.claim_id, c.member_id, p.plan_name, c.procedure, c.status
FROM claims AS c
JOIN plans AS p ON c.plan_id = p.plan_id;
```

**Output:**
```text
('C1001', 'M1001', 'Gold PPO', 'X-ray', 'Pending')
('C1002', 'M1001', 'Gold PPO', 'Surgery', 'Approved')
('C1003', 'M1002', 'Silver HMO', 'X-ray', 'Denied')
('C1004', 'M1002', 'Silver HMO', 'Surgery', 'Approved')
('C1005', 'M1003', 'Bronze HMO', 'X-ray', 'Pending')
```

## 5. Top-N query: most claimed procedures

**Question:** Which procedures were claimed the most?

```sql
SELECT procedure, COUNT(*) AS claim_count
FROM claims
GROUP BY procedure
ORDER BY claim_count DESC, procedure
LIMIT 5;
```

**Output:**
```text
('X-ray', 3)
('Surgery', 2)
```
