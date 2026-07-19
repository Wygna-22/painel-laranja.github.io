import Button from "./components/ui/Button";

function App() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#FFF8F3",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "16px",
        }}
      >
        <Button>
          Botão Primário
        </Button>

        <Button variant="secondary">
          Botão Secundário
        </Button>

        <Button variant="danger">
          Botão Perigo
        </Button>

        <Button loading>
          Salvar
        </Button>
      </div>
    </main>
  );
}

export default App;