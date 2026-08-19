from pyspark.sql import functions as F


def model(dbt, session):
    orders = dbt.ref("stg_jaffle_shop__orders")

    return (
        orders.select("id", "user_id", "order_date", "status")
        .withColumn("order_year", F.year(F.col("order_date")))
        .withColumn("is_completed", F.col("status") == F.lit("completed"))
    )
