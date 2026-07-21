import "./Colaboradores.css";
import { useState } from "react";
import { Search, Plus, Pencil, Trash2 } from "lucide-react";
import { useColaboradores } from "../../hooks/useColaboradores";
import type { Colaborador } from "../../types/colaborador";
import ColaboradorModal from "../../components/ColaboradorModal/ColaboradorModal";

export default function Colaboradores() {

    const {
        colaboradores,
        loading,
        error,
        create,
        update,
        remove,
    } = useColaboradores();

    const [pesquisa, setPesquisa] = useState("");

    const [modalOpen, setModalOpen] = useState(false);
    const [selected, setSelected] = useState<Colaborador | null>(null);

    const colaboradoresFiltrados = colaboradores.filter((colaborador) =>
        colaborador.nome.toLowerCase().includes(pesquisa.toLowerCase()) ||
        (colaborador.email ?? "").toLowerCase().includes(pesquisa.toLowerCase()) ||
        colaborador.setor.toLowerCase().includes(pesquisa.toLowerCase()) ||
        colaborador.cidade.toLowerCase().includes(pesquisa.toLowerCase())
    );

    if (loading) {
        return <h2>Carregando colaboradores...</h2>;
    }

    if (error) {
        return <h2>{error}</h2>;
    }

    return (

        <div className="colaboradores-page">

            <div className="page-header">

                <h1>Colaboradores</h1>

                <button
                    className="novo-btn"
                    onClick={() => {
                        setSelected(null);
                        setModalOpen(true);
                    }}
                >
                    <Plus size={18} />
                    Novo Colaborador
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

                    {colaboradoresFiltrados.map((colaborador) => (

                        <tr key={colaborador.id}>

                            <td>{colaborador.nome}</td>

                            <td>{colaborador.email}</td>

                            <td>{colaborador.matricula}</td>

                            <td>{colaborador.cargo}</td>

                            <td>{colaborador.setor}</td>

                            <td>{colaborador.cidade}</td>

                            <td>{colaborador.status}</td>

                            <td>

                                <button
                                    className="icon-btn"
                                    onClick={() => {
                                        setSelected(colaborador);
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
                                                `Excluir ${colaborador.nome}?`
                                            )
                                        ) {

                                            await remove(colaborador.id);

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

            <ColaboradorModal
                open={modalOpen}
                colaborador={selected}
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