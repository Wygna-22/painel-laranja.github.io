import "./Colaboradores.css";
import { useState } from "react";
import { Search, Plus, Pencil, Trash2 } from "lucide-react";

import { useGestores } from "../../hooks/useGestores";
import type { Gestor } from "../../types/gestor";
import GestorModal from "../../components/GestorModal/GestorModal";

export default function Gestores() {

    const {
        gestores,
        loading,
        error,
        create,
        update,
        remove,
    } = useGestores();

    const [pesquisa, setPesquisa] = useState("");

    const [modalOpen, setModalOpen] = useState(false);
    const [selected, setSelected] = useState<Gestor | null>(null);

    const gestoresFiltrados = gestores.filter((gestor) =>
        gestor.nome.toLowerCase().includes(pesquisa.toLowerCase()) ||
        gestor.email.toLowerCase().includes(pesquisa.toLowerCase()) ||
        gestor.setor.toLowerCase().includes(pesquisa.toLowerCase()) ||
        gestor.cidade.toLowerCase().includes(pesquisa.toLowerCase())
    );

    if (loading) {
        return <h2>Carregando gestores...</h2>;
    }

    if (error) {
        return <h2>{error}</h2>;
    }

    return (

        <div className="colaboradores-page">

            <div className="page-header">

                <h1>Gestores</h1>

                <button
                    className="novo-btn"
                    onClick={() => {
                        setSelected(null);
                        setModalOpen(true);
                    }}
                >
                    <Plus size={18} />
                    Novo Gestor
                </button>

            </div>

            <div className="pesquisa">

                <Search size={18} />

                <input
                    placeholder="Pesquisar..."
                    value={pesquisa}
                    onChange={(e) => setPesquisa(e.target.value)}
                />

            </div>

            <table className="tabela">

                <thead>

                    <tr>

                        <th>Nome</th>

                        <th>Email</th>

                        <th>Matrícula</th>

                        <th>Cargo</th>

                        <th>Setor</th>

                        <th>Cidade</th>

                        <th>Status</th>

                        <th>Ações</th>

                    </tr>

                </thead>

                <tbody>

                    {gestoresFiltrados.map((gestor) => (

                        <tr key={gestor.id}>

                            <td>{gestor.nome}</td>

                            <td>{gestor.email}</td>

                            <td>{gestor.matricula}</td>

                            <td>{gestor.cargo}</td>

                            <td>{gestor.setor}</td>

                            <td>{gestor.cidade}</td>

                            <td>{gestor.status}</td>

                            <td>

                                <button
                                    className="icon-btn"
                                    onClick={() => {
                                        setSelected(gestor);
                                        setModalOpen(true);
                                    }}
                                >
                                    <Pencil size={18} />
                                </button>

                                <button
                                    className="icon-btn delete"
                                    onClick={async () => {

                                        if (
                                            window.confirm(
                                                `Excluir ${gestor.nome}?`
                                            )
                                        ) {

                                            await remove(gestor.id);

                                        }

                                    }}
                                >
                                    <Trash2 size={18} />
                                </button>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

            <GestorModal
                open={modalOpen}
                gestor={selected}
                onClose={() => setModalOpen(false)}
                onSave={async (data) => {

                    if (selected) {

                        await update(
                            selected.id,
                            data
                        );

                    } else {

                        await create(data);

                    }

                }}
            />

        </div>

    );

}