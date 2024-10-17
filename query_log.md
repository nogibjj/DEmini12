```sql
SELECT t1.country, t1.category, t1.category,AVG(t1.Followers) as avg_followers,COUNT(*) as total_Account FROM default.InstagramData t1 JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account GROUP BY t1.country, t1.category ORDER BY avg_followers DESC LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,AVG(t1.Followers) as avg_followers,COUNT(*) as total_Account FROM default.InstagramData t1 JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account GROUP BY t1.country, t1.category ORDER BY avg_followers DESC LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,AVG(t1.Followers) as avg_followers,COUNT(*) as total_Account FROM default.InstagramData t1 JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account GROUP BY t1.country, t1.category ORDER BY avg_followers DESC LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,AVG(t1.Followers) as avg_followers,COUNT(*) as total_Account FROM default.InstagramData t1 JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account GROUP BY t1.country, t1.category ORDER BY avg_followers DESC LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

```sql
SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```

```response from databricks
[Row(country='All', category='Photography', category='Photography', avg_followers=469600000.0, total_Account=2), Row(country='All', category='Fashion|Modeling|Beauty', category='Fashion|Modeling|Beauty', avg_followers=308800000.0, total_Account=4), Row(country='All', category='Sports with a ball|Family', category='Sports with a ball|Family', avg_followers=306300000.0, total_Account=4), Row(country='All', category='Cinema|Actors/actresses|Fitness|Gym', category='Cinema|Actors/actresses|Fitness|Gym', avg_followers=295800000.0, total_Account=2), Row(country='All', category='Fashion|Beauty', category='Fashion|Beauty', avg_followers=284900000.0, total_Account=4), Row(country='All', category='Modeling|Fashion', category='Modeling|Fashion', avg_followers=217800000.0, total_Account=4), Row(country='All', category='Music|Lifestyle', category='Music|Lifestyle', avg_followers=206033333.33333334, total_Account=6), Row(country='All', category='Music|Fashion', category='Music|Fashion', avg_followers=160125000.0, total_Account=8), Row(country='All', category='Clothing|Outfits|Lifestyle', category='Clothing|Outfits|Lifestyle', avg_followers=157400000.0, total_Account=3), Row(country='All', category='Cinema|Actors/actresses|Fashion', category='Cinema|Actors/actresses|Fashion', avg_followers=127800000.0, total_Account=4)]
```

