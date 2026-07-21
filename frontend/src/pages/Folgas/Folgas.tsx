import "./Folgas.css";
import { useState } from "react";
import { Search, Plus, Pencil, Trash2 } from "lucide-react";

import { useFolgas } from "../../hooks/useFolgas";
import { useColaboradores } from "../../hooks/useColaboradores";

import type { Folga } from "../../types/folga";

import FolgaModal from "../../components/FolgaModal/FolgaModal";

export default function Folgas() {

    const {
        folgas,
        loading,
        error,
        create,
        update,
        remove,
    } = useFolgas();

    const { colaboradores } = useColaboradores();

    const [pesquisa, setPesquisa] = useState("");

    const [modalOpen, setModalOpen] = useState(false);

    const [selected, setSelected] = useState<Folga | null>(null);

    const folgasFiltradas = folgas.filter((item) => {

        const colaborador = colaboradores.find(
            (c) => c.id === item.colaborador_id
        );

        return (
            colaborador?.nome
                .toLowerCase()
                .includes(pesquisa.toLowerCase()) ?? false
        );

    });

    if (loading) return <h2>Carregando...</h2>;

    if (error) return <h2>{error}</h2>;

    return (

        <div className="folgas-page">

            <div className="page-header">

                <h1>Folgas</h1>

                <button
                    className="novo-btn"
                    onClick={() => {

                        setSelected(null);

                        setModalOpen(true);

                    }}
                >

                    <Plus size={18} />

                    Nova Folga

                </button>

            </div>

            <div className="pesquisa">

                <Search size={18} />

                <input
                    placeholder="Pesquisar colaborador..."
                    value={pesquisa}
                    onChange={(e) => setPesquisa(e.target.value)}
                />

            </div>

            <table className="tabela">

                <thead>

                    <tr>

                        <th>Colaborador</th>

                        <th>Data</th>

                        <th>Status</th>

                        <th>Motivo</th>

                        <th>Ações</th>

                    </tr>

                </thead>

                <tbody>

                    {folgasFiltradas.map((item) => {

                        const colaborador = colaboradores.find(
                            (c) => c.id === item.colaborador_id
                        );

                        return (

                            <tr key={item.id}>

                                <td>{colaborador?.nome}</td>

                                <td>{item.data}</td>

                                <td>{item.status}</td>

                                <td>{item.motivo}</td>

                                <td>

                                    <button
                                        className="icon-btn"
                                        onClick={() => {

                                            setSelected(item);

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
                                                    "Excluir folga?"
                                                )
                                            ) {

                                                await remove(item.id);

                                            }

                                        }}
                                    >

                                        <Trash2 size={18} />

                                    </button>

                                </td>

                            </tr>

                        );

                    })}

                </tbody>

            </table>

            <FolgaModal
                open={modalOpen}
                folga={selected}
                colaboradores={colaboradores}
                onClose={() => {

                    setModalOpen(false);

                    setSelected(null);

                }}
                onSave={async (data) => {

                    if (selected) {

                        await update(
                            selected.id,
                            data
                        );

                    } else {

                        await create(data);

                    }

                    setModalOpen(false);

                    setSelected(null);

                }}
            />

        </div>

    );

}