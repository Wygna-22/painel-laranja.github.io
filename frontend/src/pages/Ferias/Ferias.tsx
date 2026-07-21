import "./Ferias.css";
import { useState } from "react";
import { Search, Plus, Pencil, Trash2 } from "lucide-react";

import { useFerias } from "../../hooks/useFerias";
import { useColaboradores } from "../../hooks/useColaboradores";

import type { Ferias } from "../../services/feriasService";

import FeriasModal from "../../components/FeriasModal/FeriasModal";

export default function Ferias() {

    const {
        ferias,
        loading,
        error,
        create,
        update,
        remove,
    } = useFerias();

    const { colaboradores } = useColaboradores();

    const [pesquisa, setPesquisa] = useState("");

    const [modalOpen, setModalOpen] = useState(false);

    const [selected, setSelected] = useState<Ferias | null>(null);

    const feriasFiltradas = ferias.filter((item) => {

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

        <div className="ferias-page">

            <div className="page-header">

                <h1>Férias</h1>

                <button
                    className="novo-btn"
                    onClick={() => {

                        setSelected(null);

                        setModalOpen(true);

                    }}
                >

                    <Plus size={18} />

                    Nova Férias

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

                        <th>Início</th>

                        <th>Fim</th>

                        <th>Status</th>

                        <th>Ações</th>

                    </tr>

                </thead>

                <tbody>

                    {feriasFiltradas.map((item) => {

                        const colaborador = colaboradores.find(
                            (c) => c.id === item.colaborador_id
                        );

                        return (

                            <tr key={item.id}>

                                <td>{colaborador?.nome}</td>

                                <td>{item.data_inicio}</td>

                                <td>{item.data_fim}</td>

                                <td>{item.status}</td>

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
                                                    "Excluir férias?"
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

            <FeriasModal
                open={modalOpen}
                ferias={selected}
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