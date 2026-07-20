import "./Login.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../services/authService";

export default function Login() {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleLogin(e: React.FormEvent) {
        e.preventDefault();

        try {
            setLoading(true);
            setError("");

            const response = await login({
                username,
                password,
            });

            console.log(response);

            navigate("/dashboard");

        } catch (err) {

            console.error("ERRO:", err);

            setError("Usuário ou senha inválidos.");

        } finally {

            setLoading(false);

        }
    }

    return (
        <div className="login-page">

            <form
                className="login-card"
                onSubmit={handleLogin}
            >

                <h1>Painel Laranja</h1>

                <input
                    type="text"
                    placeholder="Usuário"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Senha"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                {error && (
                    <p className="error">
                        {error}
                    </p>
                )}

                <button
                    type="submit"
                    disabled={loading}
                >
                    {loading ? "Entrando..." : "Entrar"}
                </button>

            </form>

        </div>
    );
}