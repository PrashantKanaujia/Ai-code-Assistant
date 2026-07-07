import "./SourcesPanel.css";

function SourcesPanel({

    sources,

    onOpenFile

}) {

    return (

        <div className="sources-panel">

            <h3>Sources</h3>

            {

                sources.length === 0 ? (

                    <p>No sources.</p>

                ) : (

                    sources.map((source, index) => (

                        <div
                            key={index}
                            className="source-card"
                            onClick={() => onOpenFile(source, source)}
                        >

                            <h4>{source.file_path}</h4>

                            <p>{source.language}</p>

                        </div>

                    ))

                )

            }

        </div>

    );

}

export default SourcesPanel;