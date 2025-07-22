import React, { useState } from "react";
import { Button } from "@mui/material";
import CreateAdModal from "./CreateAdModal"; // Путь поправьте под ваш проект

export default function ExchangePage() {
  const [openCreate, setOpenCreate] = useState(false);

  const handleOpenCreate = () => setOpenCreate(true);
  const handleCloseCreate = () => setOpenCreate(false);

  // Пример массива объявлений, замените на свои реальные данные/запрос к API
  const orders = [
    {
      id: 1,
      user: "Savak",
      ordersCount: 40,
      percent: 10,
      price: "70,96",
      amount: "304,76",
      currency: "USDT",
      limits: "500 – 500 000 RUB",
      methods: ["SBP", "Банковская карта"]
    },
    {
      id: 2,
      user: "Ищу_Партнеров",
      ordersCount: 15,
      percent: 8,
      price: "71,15",
      amount: "120,00",
      currency: "USDT",
      limits: "1 000 – 200 000 RUB",
      methods: ["Банковская карта"]
    }
  ];

  return (
    <div style={{
      background: "#143524",
      minHeight: "100vh",
      fontFamily: "Inter, Arial, sans-serif",
      color: "#d1e7ce"
    }}>
      <div style={{
        background: "#10291a",
        padding: "22px 0 10px 0",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <span style={{
          fontWeight: "bold",
          fontSize: "2.1rem",
          color: "#a5f4ca",
          letterSpacing: "2px",
          marginLeft: "32px"
        }}>
          P2PExchange
        </span>
        <Button
          variant="contained"
          style={{
            background: "#3b7252",
            color: "#fff",
            fontWeight: 600,
            fontSize: "1.13rem",
            borderRadius: "10px",
            padding: "11px 28px",
            marginRight: "32px"
          }}
          onClick={handleOpenCreate}
        >
          Создать объявление
        </Button>
      </div>

      <div style={{ maxWidth: 680, margin: "26px auto", padding: "0 12px 32px 12px" }}>
        {orders.map(order => (
          <div
            key={order.id}
            style={{
              background: "#10291a",
              borderRadius: "16px",
              padding: "22px 24px 18px 24px",
              boxShadow: "0 2px 12px #14352433",
              display: "flex",
              flexDirection: "column",
              gap: "7px",
              marginBottom: "18px"
            }}
          >
            <div style={{
              display: "flex",
              gap: "22px",
              alignItems: "flex-end",
              flexWrap: "wrap"
            }}>
              <div style={{ minWidth: "180px" }}>
                <div style={{
                  display: "flex",
                  alignItems: "center",
                  gap: "8px",
                  fontSize: "1.13rem",
                  fontWeight: 600
                }}>
                  <span style={{
                    background: order.id === 1 ? "#42e26f" : "#ffd700",
                    width: "15px",
                    height: "15px",
                    borderRadius: "50%",
                    display: "inline-block"
                  }}></span>
                  <span>{order.user}</span>
                </div>
                <div style={{
                  fontSize: "0.99rem",
                  color: "#d1e7cebb",
                  fontWeight: 500
                }}>
                  {order.ordersCount} Ордеров • {order.percent}%
                </div>
              </div>
              <div style={{ minWidth: "180px" }}>
                <div style={{
                  fontSize: "1.29rem",
                  fontWeight: 700,
                  color: "#bfffcf"
                }}>
                  ₽ {order.price} <span style={{ color: "#b6f7d0", fontSize: "0.95rem" }}>{order.currency}</span>
                </div>
                <div style={{ fontSize: "1.02rem", color: "#b2e3c0" }}>
                  {order.amount} {order.currency}
                </div>
                <div style={{ fontSize: "1.02rem", color: "#b2e3c0" }}>
                  Лимиты {order.limits}
                </div>
                <div style={{ fontSize: "1.02rem", color: "#b2e3c0" }}>
                  {order.methods.map(method => (
                    <span key={method} style={{
                      background: "#1f3b28",
                      color: "#a0e7c8",
                      padding: "2px 10px",
                      borderRadius: "7px",
                      marginRight: "6px",
                      fontSize: "0.97rem"
                    }}>{method}</span>
                  ))}
                </div>
              </div>
              <div style={{ minWidth: "180px" }}>
                <div style={{
                  display: "flex",
                  gap: "11px",
                  marginTop: "8px"
                }}>
                  <Button
                    variant="contained"
                    style={{
                      background: "#2e7853",
                      color: "#fff",
                      fontWeight: 600,
                      fontSize: "1.08rem",
                      borderRadius: "10px",
                      padding: "10px 26px"
                    }}
                    href={`/exchange/buy/${order.id}/`}
                  >
                    Купить
                  </Button>
                  <Button
                    variant="outlined"
                    style={{
                      color: "#b4f7d7",
                      border: "1px solid #1f3b28",
                      borderRadius: "6px",
                      padding: "8px 18px",
                      fontSize: "1.02rem"
                    }}
                    href={`/chat/${order.id}/`}
                  >
                    Чат
                  </Button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <CreateAdModal open={openCreate} onClose={handleCloseCreate} />
    </div>
  );
}
