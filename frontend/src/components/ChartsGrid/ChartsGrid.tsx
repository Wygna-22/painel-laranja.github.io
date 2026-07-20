import "./ChartsGrid.css";

interface Props {
    children: React.ReactNode;
}

export default function ChartsGrid({ children }: Props) {
    return (
        <div className="charts-grid">
            {children}
        </div>
    );
}